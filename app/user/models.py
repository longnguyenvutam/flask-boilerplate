# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:42:56
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 06:38:44


from bcrypt import gensalt, hashpw
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import BINARY
from app import db, login_manager


class User(db.Model, UserMixin):
    """
    User model
    """

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(BINARY, nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    updated_time = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resetpasswd_token = db.Column(db.String(100), nullable=True)
    resetpasswd_time = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, user_data):
        for key, value in user_data.items():
            if key == 'password':
                value = hashpw(value.encode('utf8'), gensalt())
            setattr(self, key, value)

    def __repr__(self):
        return str(self.email)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None
