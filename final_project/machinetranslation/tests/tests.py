import unittest

from translator import english_to_french,french_to_english

class TestTranslate(unittest.TestCase):
    def test_eng_to_fr(self):
        self.assertEqual(english_to_french("hello"),"bonjour","Tests not passed")
    def test_fr_to_eng(self):
    	self.assertEqual(french_to_english("Bonjour"),"Hello","Test not passed")
if __name__ == '__main__':
    unittest.main()