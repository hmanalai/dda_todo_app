import django.http
import http

from django_declarative_apis import machinery
from django_declarative_apis.machinery import field, url_field, endpoint_resource
from .models import Todo


class TodoResourceMixin:
    consumer = None
    _consumer_type = None

    def is_authorized(self):
        return True


class TodoDefinition(TodoResourceMixin, machinery.ResourceEndpointDefinition):
    resource_model = Todo

    @endpoint_resource(type=Todo)
    def resource(self):
        return Todo.objects.all()


class TodoUpdateDefinition(TodoResourceMixin, machinery.ResourceUpdateEndpointDefinition):
    task = field(required=True, type=str)
    priority = field(required=True, type=str)
    completion_status = field(type=bool, default=False)

    @endpoint_resource(type=Todo)
    def resource(self):
        task, created = Todo.objects.get_or_create(
            task=self.task,
            priority=self.priority,
            completion_status=self.completion_status,
        )
        return task


class TodoSingleTaskDefinition(TodoResourceMixin, machinery.ResourceEndpointDefinition):
    resource_id = url_field(name='id')  # grabs the id from url

    @endpoint_resource(type=Todo)
    def resource(self):
        return Todo.objects.get(id=self.resource_id)


class TodoDeleteSingleTaskDefinition(TodoResourceMixin, machinery.ResourceEndpointDefinition):
    resource_id = url_field(name='id')

    @endpoint_resource(type=Todo)
    def resource(self):
        task = Todo.objects.get(id=self.resource_id)
        task.delete()
        return django.http.HttpResponse(status=http.HTTPStatus.OK)


class TodoUpdateSingleTaskDefinition(TodoResourceMixin, machinery.ResourceEndpointDefinition):
    task = field(required=True, type=str)
    priority = field(required=True, type=str)
    completion_status = field(type=bool, default=False)
    resource_id = url_field(name='id')

    @endpoint_resource(type=Todo)
    def resource(self):
        task = Todo.objects.get(id=self.resource_id)
        task.task = self.task
        task.priority = self.priority
        task.completion_status = self.completion_status
        task.save()
        return task


