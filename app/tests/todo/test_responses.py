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
        self.assertEqual(response.status_code, 200)

        jsonified_resp = response.json()
        self.assertEqual(jsonified_resp['task'], 'water the plants')
        self.assertEqual(jsonified_resp['priority'], 'high')
        self.assertEqual(jsonified_resp['status'], False)

        tasks = Todo.objects.all()
        assert len(tasks) == 1


    def test_get_all_tasks(self):
        task0 = Todo.objects.create(task='water the plants', priority='high', status=True)
        task1 = Todo.objects.create(task='workout', priority='high', status=False)

        get_response = self.client.get(
            f'/tasks/',
        )

        self.assertEqual(get_response.status_code, 200)

        jsonified_resp = get_response.json()
        self.assertEqual(jsonified_resp[0]['task'], 'water the plants')
        self.assertEqual(jsonified_resp[1]['task'], 'workout')


    def test_get_single_task(self):
        task = Todo.objects.create(task='water the plants', priority='high', status=True)

        get_response = self.client.get(
            f'/tasks/{task.id}/',
        )
        self.assertEqual(get_response.status_code, 200)

