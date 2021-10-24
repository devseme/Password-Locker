import unittest #Importing the unittest module
from password import Password #Importing the Password class

class testPassword(unittest.TestCase):
    '''
    Class to test Password functions
    ''' 
    def setUp(self):
        '''
        '''
        self.new_password=Password("ian","1234")

    def test_init(self): 
        self.assertEqual(self.new_password.user_name,"ian") 
        self.assertEqual(self.new_password.user_password,"1234")   



if __name__ ==  '__main__':
    unittest.main()