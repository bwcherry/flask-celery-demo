from celery import current_app
from celery.utils.log import get_task_logger
from project import models
from project.extensions import db

logger = get_task_logger(__name__)

@current_app.task
def create(username, email):
    user = models.User(
        username=username,
        email=email,
    )
    db.session.add(user)
    db.session.commit()
    logger.info('Created user id %s', user.id)

@current_app.task
def delete(id):
    user = db.session.get(models.User, id)
    db.session.delete(user)
    db.session.commit()
    logger.info('Deleted user id %s', id)
