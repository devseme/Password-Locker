class Credentials:
     '''
      initialized the user Credentials Class instances 
     '''


     credentials_list =[]
     def __init__(self, user_name, account,user_password):
        '''
        defining the properties to be shown in credentials class
        '''
        self.user_name=user_name
        self.account=account
        self.user_password=user_password

     def save_credentials(self):
          Credentials.credentials_list.append(self) 

     def delete_credentials(self):
          Credentials.credentials_list.remove(self)        
         