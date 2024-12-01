from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, EmailField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User


class LoginForm(FlaskForm): #форма регистрации пользователя
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')