# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:50:17
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 06:59:00

import secrets
import hashlib
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import app, db, login_manager
from app.user import blueprint
from app.user.models import User
from app.util import reponses

@blueprint.route('/login', methods=['POST'])
def login():
    """
    User login function
    """
    if current_user.is_authenticated:
        return jsonify(
                reponses.LOGINED
            ), 200
    try:
        data=request.json
        username=data['username']
        password=data['password']
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(reponses.BAD_REQUEST),400

    user = User.query.filter_by(username=username).first()
    if user and hashlib.md5(password.encode('utf-8')).hexdigest() == user.password:
        login_user(user)
    else:
       return jsonify(reponses.INVALID_USER),401

    return jsonify(reponses.VALID_USER),200

@blueprint.route('/register', methods=['POST'])
@login_required
def register():
    """
    User register function
    """
    user_info = {}
    

    try:
        data = request.json
        user_info['username']=data['username']
        user_info['password']=data['password']
        user_info['name']=data['name']
    except:
        return jsonify(reponses.BAD_REQUEST), 400
    try:
        user_entity=User(user_info)
        db.session.add(user_entity)
        db.session.commit()
        user_info['id'] = user_entity.id
        del user_info['password']
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(reponses.INTERNAL_SERVER_ERROR),500

    return jsonify(reponses.cre_msg('User created successfully',user_info))



@blueprint.route('/logout')
@login_required
def logout():
    """
    User logout function
    """
    try:
        logout_user
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(reponses.BAD_REQUEST),400

    return jsonify(reponses.LOGOUT),200



@blueprint.route('/changepassword', methods=['GET', 'POST'])
@login_required
def change_password():
    """
    User change their password
    """


@blueprint.route('/reset', methods=['GET', 'POST'])
def reset():
    """
    This function generate <reset_token> for the user in a period time
    """


@blueprint.route('/setpassword/<token>', methods=['GET', 'POST'])
def reset_password_with_token(token):
    """
    Set new password if the <reset_token> is valid
    """
