import pytest
from todo.models import Todo

@pytest.fixture(scope='function')
def add_task():
    def _add_task(task, priority, status):
        task = Todo.objects.create(task=task, priority=priority, status=status)
        return task
    return _add_task