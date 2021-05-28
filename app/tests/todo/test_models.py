from django.test import TestCase
from todo.models import Todo


class ModelTestCase(TestCase):
    def test_todo_model(self):
        todo = Todo(task='Water the plants', priority='important', status='False')
        todo.save()
        self.assertEqual(todo.task, 'Water the plants')
        self.assertEqual(todo.priority, 'important')
        self.assertEqual(todo.status, 'False')
        self.assertEqual(str(todo), todo.task)

