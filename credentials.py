class Credentials:
     '''
      initialized the user Credentials Class instances 
     '''


     credentials_list =[] #empty credentials list
     def __init__(self, user_name, account,user_password):
        '''
        The method defining the properties to be shown in credentials class
        '''
        self.user_name=user_name
        self.account=account
        self.user_password=user_password

     def save_credentials(self):
         '''
         Method to save the entered credentials
         '''
         Credentials.credentials_list.append(self) 

     def delete_credentials(self):
         '''
         Method to delete credentials
         '''
         Credentials.credentials_list.remove(self) 

     @classmethod
     def credentials_exists(cls,account):
         '''
         Method to check if a particular credentials exists
         '''
         for credentials in cls.credentials_list:
            if credentials.account ==account:
                return True
         return False 

     @classmethod
     def display_credentials(cls):
         '''
          method that returns the credentials list
         '''

         return cls.credentials_list
    #   @classmethod
    #   def check_password(cls,userName,userPassword)  
