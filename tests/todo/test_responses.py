import pytest

from todo.models import Todo

@pytest.mark.django_db
def test_add_task(client):
    tasks = Todo.objects.all()
    assert len(tasks) == 0

