import unittest
from main import app

class TestModule(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_card_search_route(self):
        response = self.app.get('/cardsearch.html')
        self.assertEqual(response.status_code, 200)

        rendered_content = response.get_data(as_text=True)
        self.assertIn('cardsearch.html', rendered_content)

if __name__ == '__main__':
    unittest.main()