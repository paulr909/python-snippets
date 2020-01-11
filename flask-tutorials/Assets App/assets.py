from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

js = Bundle('home.js', 'add.js', 'subtract.js', output='gen/main.js', filters='jsmin')
css = Bundle('cssfile1.css', 'cssfile2.css', 'cssfile3.css', output='gen/main.css', filters='cssmin')

assets = Environment(app)

assets.register('main_js', js)
assets.register('main_css', css)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)