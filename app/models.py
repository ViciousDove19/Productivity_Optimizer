from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    time=db.Column(db.Integer)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, content, time):
        self.content = content
        self.time = time
        self.done = False

    def __repr__(self):
        return '<Content %s>' % self.content
        return '<Content %s>' % self.time


db.drop_all()
db.create_all()