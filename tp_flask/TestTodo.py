import unittest
from Todo import Todo

class TestTodo(unittest.TestCase):

    def setUp(self):
        self.todo = Todo(1,"toto",False,12)
    
    def test_id(self):

        self.assertEqual(self.todo.id, 2)