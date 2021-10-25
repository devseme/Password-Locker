import unittest #Importing the unittest module
from password import Password #Importing the Password class

class testPassword(unittest.TestCase):
    '''
    Class to test Password functions
    ''' 
    def setUp(self):
        '''
        This is our very own self setup object that will run before others
        '''
        self.new_password=Password("ian","1234")

    def test_init(self): 
        '''
        test_init_case to test if the object is initialised correctly
        '''
        self.assertEqual(self.new_password.user_name,"ian") 
        self.assertEqual(self.new_password.user_password,"1234")  

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Password.password_list =[]

    def test_saving(self):
        '''
        test_case to test if user is saved to the list
        '''
        self.new_password.save_password()
        print(Password.password_list)
        self.assertEqual(len(Password.password_list),1)  

    def test_multiple_saves(self):
        '''
        test case to check if multiple users can be saved into the list
        '''
        self.new_password.save_password()
        another_password =Password("justine","12345")
        another_password.save_password()
        self.assertEqual(len(Password.password_list),2)

    def test_delete_password(self):
        '''
        test case to delete users from the saved list
        '''
        self.new_password.save_password()
        another_password =Password("justine","12345")
        another_password.save_password()

        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)




if __name__ ==  '__main__':
    unittest.main()