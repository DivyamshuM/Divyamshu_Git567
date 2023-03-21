import datetime
#import unittest
#from Git import getData


def my_brand(homework_name):
    print("=*=*=*= Divyamshu Mandadi =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567-A =*=*=*= ")
    print("=*=*=*= The name of the homework assignment: {} =*=*=*= ".format(homework_name))
    print("=*=*=*= Date and time: {} =*=*=*= ".format(datetime.datetime.now()))

my_brand("Homework 04a - Develop with the Perspective of the Tester in mind")

import unittest
from unittest.mock import patch
from Git import getData


class TestGit(unittest.TestCase):
    
    @patch('Git.requests.get')
    def test_getData(self, mock_requests):
        mock_response = [{'commit': {'message': 'Initial commit'}}, 
                         {'commit': {'message': 'Updated readme file'}}]
        mock_requests.return_value.json.return_value = mock_response
        
        result = getData("DivyamshuM", "Triangle567")
        self.assertEqual(result, 2)

    @patch('Git.requests.get')
    def test_getData_error(self, mock_requests):
        mock_requests.side_effect = Exception('error')
        with self.assertRaises(Exception):
            getData("DivyamshuM", "Triangle567")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
