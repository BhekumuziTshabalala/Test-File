import unittest,run
from unittest.mock import patch
from io import StringIO

class Test_Case(unittest.TestCase):
    @patch('sys.stdout',new_callable= StringIO)
    def test_run(self,output):
        output = run.print_this()
        
        self.assertEqual("This is for git",output)
        
        

if __name__ == '__main__':
    unittest.main()