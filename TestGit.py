
import unittest
from Git import getData

class TestGit(unittest.TestCase):
    
    def test_getData(self):
        result = getData("DivyamshuM", "Triangle567")
        self.assertEqual(result, 19)

    def test_getData(self):
        result = getData("ahsgdkeh", "ahsjdgs")
        self.assertNotEqual(result, 19)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()