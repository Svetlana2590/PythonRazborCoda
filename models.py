from enum import unique

from flask.cli import prepare_import
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import backref

db = SQLAlchemy() #подключение к базе данных

class TMSDB:

    class User(db.Model, UserMixin): #создание таблицы
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(150), nullable=False, unique=True) #идентификация имени
        email = db.Column(db.String(150), nullable=False, unique=True) #почты
        password = db.Column(db.String(150), nullable=False) #пароля
#поля, обязательные к заполнению
        tasks = db.relationship('Task', backref='user', lazy=True) #связь таблиц

        class Task(db.Model):  #создание второй таблицы с текстом
            id = db.Column(db.Integer, primary_key=True)
            title = db.Column(db.String(150), nullable=False)
            description = db.Column(db.Text)
            status = db.Column(db.String(20), nullable=False, default='Not started')
            user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

