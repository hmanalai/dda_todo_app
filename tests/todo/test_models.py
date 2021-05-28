import pytest

from todo.models import Todo


@pytest.mark.django_db
def test_todo_model():
    todo = Todo(task='Water the plants', priority='important', status='False')
    todo.save()
    assert todo.task == 'Water the plants'
    assert todo.priority == 'important'
    assert todo.created_date
    assert todo.status == 'False'
    assert str(todo) == todo.task

