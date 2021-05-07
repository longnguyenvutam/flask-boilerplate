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
from app.tasks.models import Tasks
from app.user.models import User
from app.util import reponses

subtask_status={
	0:'New',
	1:'In Progress',
	2:'Done',
	3:'Overdue',
	4:'Deleted'
}

@blueprint.route('/create/', methods=['POST'])
@login_required
def createSubTasks():
	subtask_info = {}

	try:
		data = request.json
		subtask_info['task_id'] = data['task_id']
		subtask_info['name'] = data['name']
		subtask_info['description'] = data['description']
		subtask_info['due_date'] = data['due_date'] 

	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST), 400
	print(subtask_info)
	try:
		subtask_entity=SubTasks(subtask_info)
		db.session.add(subtask_entity)
		db.session.commit()
		subtask_info['id'] = subtask_entity.id
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.INTERNAL_SERVER_ERROR),500

	return jsonify(reponses.cre_msg('SubTask created successfully',subtask_info))


@blueprint.route('/getall/<_task_id>', methods=['GET'])
@login_required
def getAll(_task_id):
	"""
	"""
	subtasks_all = []
	try:
		task_id  = int(_task_id)
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400

	query = SubTasks.query.filter_by(task_id=task_id).all()
	query2 = Tasks.query.filter_by(id=task_id).first()
	name = query2.name

	try:
		for item in query:
			del item._sa_instance_state
			subtasks_all.append(item.__dict__)
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.INTERNAL_SERVER_ERROR),500

	return jsonify(reponses.cre_msg(f'All subtask of task name {name} are:', subtasks_all))

@blueprint.route('/getone/<_task_id>/<_subtask_id>', methods=['GET'])
@login_required
def getOne(_task_id,_subtask_id):
	"""
	"""
	try:
		task_id = int(_task_id)
		subtask_id = int(_subtask_id)
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400

	try:
		query = SubTasks.query.filter_by(task_id=task_id,id=subtask_id).first()
		query2 = Tasks.query.filter_by(id=task_id).first()

		name = query2.name
		del query._sa_instance_state
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.INTERNAL_SERVER_ERROR),500

	return jsonify(reponses.cre_msg(f'SubTask have id {subtask_id} of Task {name} is ', query.__dict__))	

@blueprint.route('/getstatus/<_task_id>/<_subtask_id>', methods=['GET'])
@login_required
def getSubtaskStatus(_task_id,_subtask_id):
	
	try:
		task_id = int(_task_id)
		subtask_id = int(_subtask_id)
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400


	query = SubTasks.query.filter_by(id=subtask_id).first()
	query2 = Tasks.query.filter_by(id=task_id).first()

	name = query2.name
	status = subtask_status[query.status]

	return jsonify(reponses.cre_msg(f'Status of subtask have id {subtask_id} of Task {name} is', status))

@blueprint.route('/updatesubtaskstatus/<_task_id>/<_subtask_id>', methods=['PUT'])
@login_required
def updateSubTaskStatus(_task_id,_subtask_id):
	
	try:
		task_id = int(_task_id)
		subtask_id = int(_subtask_id)
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400

	try:
		data = request.json
		new_status = int(data['status'])

	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400
	if(new_status<0 or new_status > 5):
		return jsonify("Status tu 0-5"),400
	else:
		query = SubTasks.query.filter_by(task_id=task_id,id=subtask_id).first()
		query2 = Tasks.query.filter_by(id=task_id).first()

		old_status = query.status
		name = query.name
		name2 = query2.name
		query.status = new_status
		db.session.commit()

		return jsonify(f"Changed status of subtask {name} of task {name2} from {old_status} to {new_status} sucessfully")

#	return jsonify(reponses.cre_msg(f"Changed status of subtask {name} of task {name2} from {old_status} to {subtask_status} sucessfully"), )



@blueprint.route('/edit', methods=['PUT'])
def editSubTasks():
	"""
	"""

@blueprint.route('/delete/<_task_id>/<_subtask_id>', methods=['DELETE'])
@login_required
def deleteSubTasks(_task_id,_subtask_id):
	"""
	"""
	try:
		task_id = int(_task_id)
		subtask_id = int(_subtask_id)
	except Exception as e:
		app.logger.error(str(e))
		return jsonify(reponses.BAD_REQUEST),400
	query = SubTasks.query.filter_by(id=subtask_id,task_id=task_id).delete()
	db.session.commit()

	return jsonify(f"Delete successfully subtask have id {subtask_id} ")	