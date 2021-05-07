from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import (
    Integer,
    BINARY,
    DateTime,
    String,
    Text
    )
from app import db, login_manager

class SubTasks(db.Model, UserMixin):
	__tablename__ = 'SubTasks'

	id = db.Column(Integer,primary_key = True)
	task_id = db.Column(Integer, db.ForeignKey('Tasks.id'))
	name = db.Column(String(100), nullable = False)
	description = db.Column(Text, nullable = False)
	created_at = db.Column(DateTime, default = datetime.utcnow)
	due_date = db.Column(DateTime, nullable = False)
	status = db.Column(Integer, nullable = False, default = 0)
	def __init__(self, subtasks_data):
		for key, value in subtasks_data.items():
			setattr(self,key,value)