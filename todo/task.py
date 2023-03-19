from flask import (
    Blueprint, flash, g, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from todo.db import get_db

bp = Blueprint('task', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT * FROM task'
    ).fetchall()
    print(posts)
    return jsonify({'data': posts})


@bp.route('/create', methods=('GET', 'POST'))
def create():
    print(request.form)
    if request.method == 'POST':
        task_name = request.form['task_name']
        
        db = get_db()
        db.execute(
            'INSERT INTO task (task_name)'
            ' VALUES (?)',
            (task_name)
        )
        db.commit()


    return jsonify({'data': 'hey!'})

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    if request.method == 'POST':
        db = get_db()
        db.execute(
            'UPDATE task SET task_name = ?'
            ' WHERE id = ?',
            (task_name, id)
        )
        db.commit()

    return jsonify({'data': 'hey'})


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    db = get_db()
    db.execute('DELETE FROM task WHERE id = ?', (id,))
    db.commit()
    return jsonify({'data': 'success'})
