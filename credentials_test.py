import unittest #Importing the unittest module
from credentials import Credentials #Importing the Credentials class

class testCredentials(unittest.TestCase):
    '''
    Class to test Credentials functions
    '''   
    def setUp(self):
        '''
        '''
        self.new_credentials=Credentials("ian","twitter","1234")

    def test_init(self): 
        self.assertEqual(self.new_credentials.user_name,"ian") 
        self.assertEqual(self.new_credentials.account,"twitter")  
        self.assertEqual(self.new_credentials.user_password,"1234")  

if __name__ ==  '__main__':
    unittest.main()