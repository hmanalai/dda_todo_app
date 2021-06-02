from django.test import TestCase
from todo.models import Todo

class ResponseTestCase(TestCase):
    def test_add_task(self):
        tasks = Todo.objects.all()
        self.assertEqual(len(tasks), 0)

        response = self.client.post(
            '/tasks/',
            {
                'task': 'water the plants',
                'priority': 'high',
                'completion_status': False,
             }
        )
        self.assertEqual(response.status_code, 200)

        jsonified_resp = response.json()
        self.assertEqual(jsonified_resp['task'], 'water the plants')
        self.assertEqual(jsonified_resp['priority'], 'high')
        self.assertEqual(jsonified_resp['completion_status'], False)

        tasks = Todo.objects.all()
        self.assertEqual(len(tasks), 1)


    def test_add_task_invalid_json(self):
        tasks = Todo.objects.all()
        self.assertEqual(len(tasks),  0)

        response = self.client.post(
            '/tasks/',
            {},
        )
        self.assertEqual(response.status_code, 400)

        tasks = Todo.objects.all()
        self.assertEqual(len(tasks), 0)


    def test_add_task_invalid_json_keys(self):
        tasks = Todo.objects.all()
        self.assertEqual(len(tasks),  0)

        response = self.client.post(
            '/tasks/',
            {'status': False},
        )
        self.assertEqual(response.status_code, 400)

        tasks = Todo.objects.all()
        self.assertEqual(len(tasks), 0)


    def test_get_all_tasks(self):
        task0 = Todo.objects.create(task='water the plants', priority='high', completion_status=True)
        task1 = Todo.objects.create(task='workout', priority='high', completion_status=False)

        response = self.client.get(f'/tasks/',)

        self.assertEqual(response.status_code, 200)

        jsonified_resp = response.json()
        self.assertEqual(jsonified_resp[0]['task'], 'water the plants')
        self.assertEqual(jsonified_resp[1]['task'], 'workout')


    def test_get_single_task(self):
        task = Todo.objects.create(task='water the plants', priority='high', completion_status=True)

        response = self.client.get(f'/tasks/{task.id}/',)
        self.assertEqual(response.status_code, 200)

        jsonified_resp = response.json()
        self.assertEqual(jsonified_resp['task'], 'water the plants')


    def test_get_single_task_incorrect_id(self):
        response = self.client.get(f'/tasks/foo/')
        self.assertEqual(response.status_code, 404)


    def test_delete_sinlge_task(self):
        task = Todo.objects.create(task='water the plants', priority='high', completion_status=True)

        response = self.client.get(f'/tasks/{task.id}/',)
        self.assertEqual(response.status_code, 200)

        jsonified_resp = response.json()
        self.assertEqual(jsonified_resp['task'], 'water the plants')

        delete_response = self.client.delete(f'/tasks/{task.id}/')
        self.assertEqual(delete_response.status_code, 200)


    def test_delete_single_task_incorrect_id(self):
        response = self.client.get(f'/tasks/200/')
        self.assertEqual(response.status_code, 404)


    def test_update_single_task(self):
        task = Todo.objects.create(task='Water the plants', priority='Important', completion_status=False)

        update_response = self.client.post( # put
            f'/tasks/{task.id}/',
            {
                'task': 'do laundry',
                'priority': 'low',
                'completion_status': False
            },
        )
        self.assertEqual(update_response.status_code, 200)

        jsonified_resp = update_response.json()
        self.assertEqual(jsonified_resp['task'], 'do laundry')


    def test_update_task_incorrect_id(self):
        response = self.client.post(f'/tasks/200/')  # put
        self.assertEqual(response.status_code, 404)


    def test_update_task_incorrect_json(self):
        task = Todo.objects.create(task='Water the plants', priority='Important', completion_status=False)

        update_response = self.client.post(  # put
            f'/tasks/{task.id}/',
            {},
        )
        self.assertEqual(update_response.status_code, 400)


    def test_update_task_incorrect_json_keys(self):
        task = Todo.objects.create(task='Water the plants', priority='Important', completion_status=False)

        update_response = self.client.post(   # put
            f'/tasks/{task.id}/',
            {
                'title': 'water the plants',
                'priority': 'low',
            },
        )
        self.assertEqual(update_response.status_code, 400)
