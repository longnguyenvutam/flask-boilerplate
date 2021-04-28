from flask import Blueprint


blueprint = Blueprint(
    'tasks_blueprint',
    __name__,
    url_prefix='/tasks'
)
