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

    def tearDown(self):
        Password.password_list =[]
        
    def test_saving(self):
        self.new_password.save_password()
        print(Password.password_list)
        self.assertEqual(len(Password.password_list),1)  

    def test_multiple_saves(self):
        self.new_password.save_password()
        another_password =Password("justine","12345")
        another_password.save_password()
        self.assertEqual(len(Password.password_list),2)



if __name__ ==  '__main__':
    unittest.main()