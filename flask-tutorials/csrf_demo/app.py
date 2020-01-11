from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/csrf_demo/csrf.db'
app.config['SECRET_KEY'] = 'hereisasecretkey'
app.config['WTF_CSRF_ENABLED'] = True

login_manager = LoginManager(app)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class EmailForm(FlaskForm):
    email_address = StringField('Email')

@app.route('/login')
def login():
    user = User.query.get(1)
    login_user(user)
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/updateemail', methods=['GET', 'POST'])
@login_required
def updateemail():
    form = EmailForm()

    if form.validate_on_submit():
        current_user.email_address = form.email_address.data
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('email.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)