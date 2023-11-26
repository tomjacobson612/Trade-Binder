import unittest
from dbmodel import model

class TestAdd(unittest.TestCase):
    
    def test_add_card_null_name(self):
        self.assertEqual(False, model().insert(None, 1, "http://testimage.com/1.jpg"))
    
    def test_add_card_null_num(self):
        self.assertEqual(False, model().insert("Charizard", None, "http://testimage.com/1.jpg"))
    
    def test_add_card_null_img(self):
        self.assertEqual(False, model().insert("Charizard", 1, None))

    def test_add_card(self):
        self.assertEqual(True, model().insert("Charizard", 1, "http://testimage.com/1.jpg"))

if __name__ == '__main__':
    unittest.main()