import unittest #Importing the unittest module
from credentials import Credentials #Importing the Credentials class
class testCredentials(unittest.TestCase):
    '''
    Class to test Credentials functions
    '''   
    def setUp(self):
        '''
        This is the set up method that will run before each test case
        '''
        self.new_credentials=Credentials("ian","twitter","1234")

    def test_init(self): 
        '''
        test_init case to test if our own object is initialized correctly
        '''
        self.assertEqual(self.new_credentials.user_name,"ian") 
        self.assertEqual(self.new_credentials.account,"twitter")  
        self.assertEqual(self.new_credentials.user_password,"1234") 

    def tearDown(self):
        '''
         tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list =[]

    def test_saving(self):
        '''
        test case to save our initilaised object
        '''
        self.new_credentials.save_credentials()
        print(Credentials.credentials_list)
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_multiple_saves(self):
        '''
        test case to check if multiple objects can be saved
        '''
        self.new_credentials.save_credentials()
        another_credentials =Credentials("justine","Instagram","12345")
        another_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)  

    def test_delete_Credentials(self):
        '''
        test case to delete a saved credential from our credentials_list
        '''
        self.new_credentials.save_credentials()
        another_credentials =Credentials("justine","Instagram","12345")
        another_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)  

    def test_check_credentials_exists(self): 
        '''
        test case to check if a particular credential exists
        '''
        self.new_credentials.save_credentials()
        another_credentials =Credentials("justine","Instagram","12345")
        another_credentials.save_credentials()

        credentials_exists=Credentials.credentials_exists("Instagram")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)



if __name__ ==  '__main__':
    unittest.main()