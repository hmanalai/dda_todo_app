from django_declarative_apis.machinery import filtering
from .models import Todo

TodoResponseFilter = {
    Todo: {
        'task': filtering.ALWAYS,
        'priority': filtering.ALWAYS,
        'created_date': filtering.ALWAYS,
        'completion_status': filtering.ALWAYS
    },
}