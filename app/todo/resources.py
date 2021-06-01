from django_declarative_apis import machinery
from django_declarative_apis.machinery import filtering, field, url_field
from .models import Todo


class TodoDefinition(machinery.ResourceEndpointDefinition):
    consumer = None
    _consumer_type = None
    resource_model = Todo

    def is_authorized(self):
        return True

    @machinery.endpoint_resource(
        type=Todo,
        filter={
            Todo: {'task': filtering.ALWAYS,
                   'priority': filtering.ALWAYS,
                   'created_date': filtering.ALWAYS,
                   'status': filtering.ALWAYS},
        },
    )
    def resource(self):
        return Todo.objects.all()


class TodoUpdateDefinition(machinery.ResourceUpdateEndpointDefinition):
    consumer = None
    _consumer_type = None

    task = field(required=True, type=str)
    priority = field(required=True, type=str)
    status = field(type=bool)

    def is_authorized(self):
        return True

    @machinery.endpoint_resource(
        type=Todo,
        filter={
                 Todo: {'task': filtering.ALWAYS,
                        'priority': filtering.ALWAYS,
                        'created_date': filtering.ALWAYS,
                        'status': filtering.ALWAYS},
                 },
    )
    def resource(self):
        task, created = Todo.objects.get_or_create(
            task=self.task,
            priority=self.priority,
            status=self.status,
        )
        return task


class TodoSingleTaskDefinition(machinery.ResourceEndpointDefinition):
    consumer = None
    _consumer_type = None
    resource_id = url_field(name='id')

    def is_authorized(self):
        return True

    @machinery.endpoint_resource(
        type=Todo,
        filter={
            Todo: {'task': filtering.ALWAYS,
                   'priority': filtering.ALWAYS,
                   'created_date': filtering.ALWAYS,
                   'status': filtering.ALWAYS},
            },
    )
    def resource(self):
        return Todo.objects.get(id=self.resource_id)
