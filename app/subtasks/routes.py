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
from app.subtasks import blueprint
from app.subtasks.models import SubTasks

@blueprint.route('/create', methods=['POST'])
def createSubTasks():
	"""
	"""
@blueprint.route('/getall', methods=['GET'])
def getAll():
	"""
	"""
@blueprint.route('/getone', methods=['GET'])
def getOne():
	"""
	"""
@blueprint.route('/edit', methods=['PUT'])
def editSubTasks():
	"""
	"""
@blueprint.route('/delete', methods=['DELETE'])
def deleteSubTasks():
	"""
	"""