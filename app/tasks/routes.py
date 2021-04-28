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
from app.tasks import blueprint
from app.tasks.models import Tasks

@blueprint.route('/create',methods=['POST'])
def create():


@blueprint.route('/getall',methods=['GET'])
def getAll():


@blueprint.route('/getone', methods=['GET'])
def getOne():


@blueprint.route('/edittask', methods=['PUT'])
def editTask():


@blueprint.route('/deletetask', methods=['DELETE'])
def deleteTask()