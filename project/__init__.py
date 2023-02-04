# This is written with the following ethos
# GLOBAL VARIABLES ARE EVIL

def create_app():
    # Imports here keep things out of the global scope
    # Its only available in the local scope
    from flask import Flask

    flask_app = Flask(__name__)
    flask_app.config.from_object('config.settings')
    celery_app = init_celery(flask_app)

    init_extensions(flask_app)
    init_db(flask_app)
    init_blueprints(flask_app)

    return flask_app, celery_app

def init_celery(app):
    from celery import Celery

    celery = Celery(app.import_name)
    celery.conf.update(app.config['CELERY_CONFIG'])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

def init_db(app):
    from project.extensions import db
    with app.app_context():
        from project import models
        # We need to import all our models
        # so that when we call db.create_all
        # SQLAlchemy has everything it needs to create our tables
        db.create_all()

def init_extensions(app):
    from project.extensions import db
    db.init_app(app)

def init_blueprints(app):
    from project.users import bp
    app.register_blueprint(bp, url_prefix='/')
