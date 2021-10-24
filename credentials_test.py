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

    def tearDown(self):
        Credentials.credentials_list =[]

    def test_saving(self):
        self.new_credentials.save_credentials()
        print(Credentials.credentials_list)
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_multiple_saves(self):
        self.new_credentials.save_credentials()
        another_credentials =Credentials("justine","Instagram","12345")
        another_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)    


if __name__ ==  '__main__':
    unittest.main()