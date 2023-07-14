from flask import Flask, render_template, flash, redirect, url_for, session, logging,request
#from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from data import Articles
app=Flask(__name__)
app.secret_key='mini flask app'

Articles=Articles()

@app.route('/')
def index():
	return render_template("indexX.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/member')
def member():
	return render_template("member.html")

@app.route('/list')
def about():
	return render_template("list.html")

@app.route('/cart')
def about():
	return render_template("cart.html")


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])	


@app.route('/register', methods=['GET','POST'])
def register():
	form=RegisterForm(request.form)
	if request.method=='POST' and form.validate():
		name=form.name.data
		email=form.email.data
		username=form.username.data
		password=sha256_crypt.encrypt(form.password.data)

		cur=mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, email, password) VALUES (%s,%s,%s,%s)"),(name,email,username,password)
		
		mysql.connection.commit()


		cur.close()
		
		return render_template('register.html')
	return render_template('register.html', form=form)


#@app.route('/articles')
#def about():
#	return render_template("articles.html", articles=Articles)

#@app.route('/articles/<string:id>')
#def about():
#	return render_template("articles.html", id=id)




if __name__=='__main__':
	app.run(debug=True)
