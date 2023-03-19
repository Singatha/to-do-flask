from flask import (
    Blueprint, flash, g, request, url_for, jsonify
)
from werkzeug.exceptions import abort
import json
from todo.db import get_db

bp = Blueprint('task', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT * FROM task'
    ).fetchall()

    return jsonify({'data': posts[0]['id']})


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        data = request.get_json()
        task_name = data['task_name']
        print(task_name)
        
        db = get_db()
        db.execute(
            'INSERT INTO task (task_name)'
            ' VALUES (?)',
            (task_name,)
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
