class Password:
     '''
      initialized the user Password Class instances.Here we store our users list 
     '''


     password_list =[] #empty users list
     def __init__(self,userName,userPassword):
         '''
         Method to define the properties of our users
         '''
         self.user_name=userName
         self.user_password=userPassword

     def save_password(self):
         '''
         method to save a user in our users_list
         '''
         Password.password_list.append(self)

     def delete_password(self):
         '''
         method to delete a user from our users_list
         '''
         Password.password_list.remove(self)
