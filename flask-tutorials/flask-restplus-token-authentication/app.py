from flask import Flask, Blueprint, request
from flask_restplus import Api, Resource, fields
from marshmallow import Schema, fields as ma_fields, post_load
from functools import wraps 

app = Flask(__name__)
#blueprint = Blueprint('api', __name__, url_prefix='/api')
#api = Api(blueprint, doc='/documentation') #,doc=False

#app.register_blueprint(blueprint)

authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'X-API-KEY'
    }
}

api = Api(app, authorizations=authorizations)

#app.config['SWAGGER_UI_JSONEDITOR'] = True

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Token is missing.'}, 401

        if token != 'mytoken':
            return {'message' : 'Your token is wrong, wrong, wrong!!!'}, 401

        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated


class TheLanguage(object):
    def __init__(self, language, framework):
        self.language = language
        self.framework = framework 

    def __repr__(self):
        return '{} is the language. {} is the framework.'.format(self.language, self.framework)

class LanguageSchema(Schema):
    language = ma_fields.String()
    framework = ma_fields.String()

    @post_load
    def create_language(self, data):
        return TheLanguage(**data)
 
a_language = api.model('Language', {'language' : fields.String('The language.'), 'framework' : fields.String('The framework')})

languages = []
#python = {'language' : 'Python', 'id' : 1}
python = TheLanguage(language='Python', framework='Flask')
languages.append(python)

@api.route('/language')
class Language(Resource):

    #@api.marshal_with(a_language, envelope='the_data')
    @api.doc(security='apikey')
    @token_required
    def get(self):
        schema = LanguageSchema(many=True)

        return schema.dump(languages)

    @api.expect(a_language)
    def post(self):
        schema = LanguageSchema()

        new_language = schema.load(api.payload)
        #new_language['id'] = len(languages) + 1
        languages.append(new_language.data)
        return {'result' : 'Language added'}, 201 

if __name__ == '__main__':
    app.run(debug=True)