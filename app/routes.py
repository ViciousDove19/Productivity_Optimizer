from app import app
from app.models import db,Task
from flask import request, jsonify, render_template, redirect


@app.route('/')
def tasks_list():
    tasks = Task.query.all()
    return render_template('list.html', tasks=tasks)


@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        return 'Error'

    time = request.form['time']
    if not time:
    	return 'Error'

    task = Task(content, time)
    db.session.add(task)
    db.session.commit()
    return redirect('/')

@app.route('/schedule', methods=['POST'])
def schedule():
	tasks = Task.query.order_by(Task.time.asc()).all()
	return render_template('list.html', tasks=tasks)


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return redirect('/')
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect('/')