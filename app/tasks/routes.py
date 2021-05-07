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
from app.user.models import User
from app.util import reponses

task_status={
	0:'New',
	1:'In Progress',
	2:'Done',
	3:'Overdue',
	4:'Deleted'
}

@blueprint.route('/create/',methods=['POST'])
@login_required
def create(): 
	"""
	"""
	tasks_info = {}
	

	try:
		data = request.json
		tasks_info['user_id']=data['user_id']
		tasks_info['name']=data['name']
		tasks_info['description']=data['description']
		tasks_info['due_date']=data['due_date']
	except:
		return jsonify(reponses.BAD_REQUEST), 400
	try:
		task_entity=Tasks(tasks_info)
		db.session.add(task_entity)
		db.session.commit()
		tasks_info['id'] = task_entity.id
		del tasks_info['user_id']
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.INTERNAL_SERVER_ERROR),500

	return jsonify(reponses.cre_msg('Task created successfully',tasks_info))

@blueprint.route('/getall/<_user_id>',methods=['GET'])
@login_required
def getAll(_user_id):
	"""
	"""
	tasks_all=[]
	try:
		user_id = int(_user_id)
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400

	query = Tasks.query.filter_by(user_id=user_id).all()
	query2 = User.query.filter_by(id=user_id).first()
	name = query2.name

	for item in query:
		del item._sa_instance_state
		tasks_all.append(item.__dict__)

	return jsonify(reponses.cre_msg(
		f"All task: {str(name)}", tasks_all))

	#return jsonify(reponses.SUCCESS("All tasks of user " + str(name), tasks_all))

@blueprint.route('/getone/<_user_id>/<_task_id>', methods=['GET'])
@login_required
def getOne(_user_id,_task_id):
	"""
	"""
	try:
		user_id = int(_user_id)
		task_id = int(_task_id)
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400		
	try:
		query = Tasks.query.filter_by(user_id=user_id,id=task_id).first()
		query2 = User.query.filter_by(id=user_id).first()

		name = query2.name
		del query._sa_instance_state

		return jsonify(reponses.cre_msg(f"Task of user {str(name)} have task_id {task_id} is: ", query.__dict__))
	
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400

@blueprint.route('/edittask', methods=['PUT'])
def editTask():
	"""
	"""

@blueprint.route('/deletetask', methods=['DELETE'])
def deleteTask():
	"""
	"""