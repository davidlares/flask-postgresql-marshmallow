from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class TaskSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'deadline')

class ParamsTaskSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=50))
    description = fields.Str(required=True, validate=Length(max=200))
    deadline = fields.DateTime(required=True)

# serializing task objects
task_schema = TaskSchema()
# same schema but for multiple items (list)
tasks_schema = TaskSchema(many=True)
# params handling
params_task_schema = ParamsTaskSchema()
