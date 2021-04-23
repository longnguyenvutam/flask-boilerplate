# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:50:17
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 06:59:00


import secrets
from bcrypt import checkpw, hashpw, gensalt
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from hashlib import sha256
from app import app, db, login_manager
from app.user import blueprint
from app.user.models import User


@blueprint.route('/login', methods=['POST'])
def login():
    """
    User login function
    """


@blueprint.route('/register', methods=['POST'])
def register():
    """
    User register function
    """


@blueprint.route('/logout')
@login_required
def logout():
    """
    User logout function
    """


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
