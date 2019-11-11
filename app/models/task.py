# ORM
from . import db
# action listener
from sqlalchemy.event import listen
from sqlalchemy import desc, asc

# db.model inheritance
class Task(db.Model):

    __tablename__ = 'tasks'

    # table columns description
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    # add new task (class method)
    @classmethod
    def new(cls, title, description, deadline):
        return Task(title=title,description=description, deadline=deadline)

    @classmethod
    def get_by_page(cls, order, current, per_page=10):
        # sorting rules
        sort = desc(Task.id) if order == 'desc' else asc(Task.id)
        # paginate object
        return Task.query.paginate(current, per_page).items # we get the task list

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            return False

    def __str__(self):
        return self.title

    def serialize(self):
        # serializing results
        return {'id': self.id, 'title': self.title, 'description': self.description, 'deadline': self.deadline}

def insert_tasks(*args, **kwargs):
    db.session.add(Task(title="Title 1",description="Description 1", deadline='2020-01-01 12:00:00'))
    db.session.add(Task(title="Title 2",description="Description 2", deadline='2020-01-01 12:00:00'))
    # persist data
    db.session.commit()

# this listener is for creating dummy data after table creation
listen(Task.__table__, 'after_create', insert_tasks)
