import unittest
import os
from app import app, db, Task

class BasicTests(unittest.TestCase):

    # Setup is run before each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Use an in-memory database for tests
        self.app = app.test_client()
        db.create_all()

    # Teardown is run after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Test 1: Ensure the main page loads correctly
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'My To-Do List', response.data)

    # Test 2: Ensure a task can be added
    def test_add_task(self):
        # Post a new task to the /add endpoint
        self.app.post('/add', data=dict(content='A new test task'), follow_redirects=True)

        # Check if the task was added to the database
        task = Task.query.filter_by(content='A new test task').first()
        self.assertIsNotNone(task)

if __name__ == "__main__":
    unittest.main()
