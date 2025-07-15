from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyEmailClassifier(FlaskForm):
    email = StringField("Enter Email: ", validators=[DataRequired()])
    submit = SubmitField('Submit')