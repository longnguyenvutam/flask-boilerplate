from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import (
    Integer,
    DateTime,
    String,
    Text
    )
from app import db, login_manager

class Tasks(db.Model, UserMixin):
	__tablename__ = 'Tasks'

	id = db.Column(Integer, primary_key = True)
	user_id = db.Column(Integer,db.ForeignKey('User.id'),nullable = False)
	name = db.Column(String(100), nullable = False)
	description = db.Column(Text, nullable = False)
	create_at = db.Column(DateTime, default = datetime.utcnow)
	update_at = db.Column(DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)
	due_date = db.Column(DateTime, nullable = False)
	status = db.Column(Integer, nullable = False, default = 0)

	def __init__(self, tasks_data):
		for key,value in tasks_data.items():
			setattr(self,key,value)

	def __repr__(self):
		return str(self.user_id)
