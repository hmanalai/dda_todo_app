from django.test import TestCase
from todo.models import Todo

class ResponseTestCase(TestCase):
    def test_add_task(self):
        tasks = Todo.objects.all()
        assert len(tasks) == 0

        response = self.client.post(
            '/tasks/',
            {
                'task': 'water the plants',
                'priority': 'high',
                'status': False,
             }
        )
        print('Response: ', response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['task'], 'water the plants')

