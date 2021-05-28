import json
import django.http

from django_declarative_apis import machinery
from django_declarative_apis.machinery import filtering
from .models import Todo


class TodoResourceMixin:
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
        return Todo.objects.get(pk=self.resource_id)


class TodoDefinition(TodoResourceMixin, machinery.ResourceEndpointDefinition):
    resource_model = Todo

    def is_authorized(self):
        return True


class TodoUpdateDefinition(TodoResourceMixin, machinery.ResourceUpdateEndpointDefinition):
    resource_model = Todo  # ASSUMPTION: I only need to pass the fields required for the TODO model

    def is_authorized(self): # Is this required? If so, why?
        return True

    @machinery.task  # Is this how the todo instance is saved to the database?
    def save(self):
        self.resource.save()
