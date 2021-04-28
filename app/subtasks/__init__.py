from flask import Blueprint


blueprint = Blueprint(
    'subtasks_blueprint',
    __name__,
    url_prefix='/subtasks'
)
