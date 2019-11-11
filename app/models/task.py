# ORM
from . import db
# action listener
from sqlalchemy.event import listen

# db.model inheritance
class Task(db.Model):

    __tablename__ = 'tasks'

    # table columns description
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    def __str__(self):
        return self.title

def insert_tasks(*args, **kwargs):
    db.session.add(Task(title="Title 1",description="Description 1", deadline='2020-01-01 12:00:00'))
    db.session.add(Task(title="Title 2",description="Description 2", deadline='2020 -01-01 12:00:00'))
    # persist data
    db.session.commit()

# this listener is for creating dummy data after table creation
listen(Task.__table__, 'after_create', insert_tasks)
