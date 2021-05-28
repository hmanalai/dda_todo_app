import json
import django.http

from django_declarative_apis import machinery
from django_declarative_apis.machinery import filtering, field
from .models import Todo


# class TodoResourceMixin:
#     @machinery.endpoint_resource(
#         type=Todo,
#         filter={
#             Todo: {'task': filtering.ALWAYS,
#                    'priority': filtering.ALWAYS,
#                    'created_date': filtering.ALWAYS,
#                    'status': filtering.ALWAYS},
#         },
#     )
#     def resource(self):
#         return Todo.objects.get(pk=self.resource_id)


class TodoDefinition(machinery.ResourceEndpointDefinition):
    resource_model = Todo

    def is_authorized(self):
        return True


class TodoUpdateDefinition(machinery.ResourceUpdateEndpointDefinition):
    consumer = None
    _consumer_type = None   # Ask about this?

    # field: name --> the name on json, that will be converted to the field here.

    task = field(required=True, type=str)   # What are all the fields that a field takes?
    priority = field(required=True, type=str)
    status = field(type=bool)

    def is_authorized(self):  # Ask about this? Is it required?
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
        print("Hiiii!")
        task, created = Todo.objects.get_or_create(
            task=self.task,
            priority=self.priority,
            status=self.status,
        )
        return task


