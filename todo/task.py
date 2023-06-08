from flask import (
    Blueprint, flash, g, request, url_for, jsonify
)
from werkzeug.exceptions import abort
import json
from todo.db import get_db

bp = Blueprint('task', __name__)

@bp.route('/tasks')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT * FROM task'
    ).fetchall()

    return jsonify({'data': posts[0]['task_name']})

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        data = request.get_json()
        task_name = data['task_name']
        task_description = data['task_description']
        task_status = data['task_status']
        
        db = get_db()
        db.execute(
            'INSERT INTO task (task_name, task_description, task_status)'
            ' VALUES (?, ?, ?)',
            (task_name, task_description, task_status)
        )
        db.commit()

    return jsonify({'data': 'hey!'})

@bp.route('/update/<int:id>', methods=('PUT', 'POST'))
def update(id):
    if request.method == 'POST':
        data = request.get_json()
        task_name = data['task_name']
        task_description = data['task_description']
        task_status = data['task_status']
        db = get_db()
        db.execute(
            'UPDATE task SET task_name = ?, task_description = ?, task_status = ?'
            ' WHERE task_id = ?',
            (task_name, task_description, task_status, id)
        )
        db.commit()

    return jsonify({'data': 'hey'})

@bp.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    db = get_db()
    db.execute('DELETE FROM task WHERE task_id = ?', (id,))
    db.commit()
    return jsonify({'data': 'success'})
