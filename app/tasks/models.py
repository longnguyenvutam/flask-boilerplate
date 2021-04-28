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

class Tasks(db.Model, UserMixin):
	__tablename__ = 'Tasks'

	id = db.Column(Integer, primary_key = True)
	user_id = db.Column(Integer, nullable = False)
	name = db.Column(String(100), nullable = False)
	description = db.Column(Text, nullable = False)
	create_at = db.Column(DateTime, default = datetime.utcnow)
	update_at = db.Column(DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)
	due_date = db.Column(DateTime, nullable = False)

	def __init__(self, tasks_data):
		for value,key in tasks_data.items():
			setattr(self,key,value)