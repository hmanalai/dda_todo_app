import pytest

from todo.models import Todo

@pytest.mark.django_db
def test_add_task(client):
    tasks = Todo.objects.all()
    assert len(tasks) == 0

    response = client.post(
        '/tasks/',
        {
            'task': 'water the plants',
            'priority': 'high',
            'status': False,
         }
    )
    print('Response: ', response.json())
    assert response.status_code == 200
    assert response.json()['task'] == 'water the plants'

