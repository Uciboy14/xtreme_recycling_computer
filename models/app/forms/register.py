from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(4, 40)])
    email = StringField("Email", validators=[DataRequired(), Length(6, 64), Email()])
    password = PasswordField("New Password", validators=[DataRequired()])
    confirm_password = PasswordField("Repeat Password", validators=[DataRequired()]) #EqualTo('password', message="Passwords must match"))
    submit = SubmitField('Register ')