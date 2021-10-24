class Password:
     '''
      initialized the instances 
     '''


     password_list =[]
     def __init__(self,userName,userPassword):
         self.user_name=userName
         self.user_password=userPassword

     def save_password(self):
          Password.password_list.append(self)

     def delete_password(self):
          Password.password_list.remove(self)
