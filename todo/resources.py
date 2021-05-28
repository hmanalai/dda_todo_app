import json
import django.http

from django_declarative_apis import machinery
from django_declarative_apis.machinery import filtering
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
            task='',
            priority='',
            status='',
        )

        return task


