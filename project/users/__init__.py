from time import sleep
from flask import Blueprint, redirect, render_template, request, url_for
from project import models
from project.extensions import db
from . import tasks

bp = Blueprint('users', __name__, template_folder='templates')

@bp.route('/')
def index():
    stmt = db.select(models.User).order_by(models.User.username)
    users = db.session.execute(stmt).scalars()
    return render_template('users/index.html', users=users)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        tasks.create.delay(request.form['username'], request.form['email'])
        # REMEMBER! This is just a demo, not a complete solution
        #
        # If we didn't sleep here this could run so fast
        # that when we redirect the changes to the records
        # were not reflected on the redirect
        sleep(0.3)
        return redirect(url_for('.index'))
    return render_template('users/create.html')

@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    user = db.get_or_404(models.User, id)
    if request.method == 'POST':
        tasks.delete.delay(id)
        sleep(0.3)
        return redirect(url_for('.index'))
    return render_template('users/delete.html', user=user)
