class Credentials:
     '''
      initialized the user Credentials Class instances 
     '''


     credential_list =[]
     def __init__(self, user_name, account,user_password):
        '''
        defining the properties to be shown in credentials class
        '''
        self.user_name=user_name
        self.account=account
        self.user_password=user_password
         