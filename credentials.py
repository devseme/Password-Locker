class Credentials:
     '''
      initialized the user Credentials Class instances 
     '''


     credential_list =[]
     def __init__(self, user_name, account, account_username, user_password):
        '''
        defining the properties to be shown in credentials class
        '''
        self.user_name=user_name
        self.account=account
        self.account_username=account_username
        self.user_password=user_password
         