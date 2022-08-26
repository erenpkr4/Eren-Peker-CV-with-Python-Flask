from flask import Flask, redirect, render_template, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators

app = Flask(__name__)
app.config['SECRET_KEY'] = '32kjsdfsdgsd2332trf'

class NameForm(FlaskForm):
    name = StringField('', validators=[validators.DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'), 404

@app.route('/')
def redirect_to_homepage():

    return redirect('/home')

@app.route('/home', methods=['GET','POST'])
def home():
    name = None
    name_form = NameForm()
    
    if name_form.validate_on_submit():
        session['name'] = name_form.name.data
        return redirect(url_for('home'))

    return render_template('home.html', name_form=name_form, name = session.get('name'))

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/experience')
def experience():
    
    return render_template('experience.html')

@app.route('/education')
def education():

    return render_template('education.html')

@app.route('/skillslanguages')
def skillslanguages():

    return render_template('skillslanguages.html')

@app.route('/certification')
def certification():

    return render_template('certification.html')
"""
@app.route('/clear')
def clear():
    session.clear()
    return render_template('404.html')
"""



if __name__ == '__main__':
    app.run(debug=False)