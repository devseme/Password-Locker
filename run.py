#!/usr/bin/env python3.8
import string
import random

from password import Password
from credentials import Credentials

def create_password(userName,userPassword):
    '''
    Function to create a new user in our password class
    '''
    new_password = Password(userName,userPassword)
    return new_password

def save_password(Password):
    '''
    Function to save users in our password class
    '''
    Password.save_password()
def delete_password(Password):
    '''
    Function to save users in our password class
    '''
    Password.delete_password()


def generate_password(length=7):
    '''
    Function that allows users to generate passwords
    '''
    # gen_pass = Credentials.generate_password()
    # return gen_pass
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))



def create_credentials(user_name, account,user_password):
    '''
    Function to create new credential in Credentials class
    '''
    new_credentials = Credentials(user_name, account,user_password)
    return new_credentials

def save_credentials(Credentials):
    '''
    Function to save credentials in credentials class
    '''
    Credentials.save_credentials()

def delete_credentials(Credentials):
    '''
    Function to delete credentials in credential class
    '''
    Credentials.delete_credentials()

def check_credentials_exists(Credentials):
    '''
    Function to check if the credentials exists in credential class
    '''
    Credentials.credentials_exists()

def display_credentials(Credentials):
    '''
    returns all the saved credentials in our Credentials class
    '''
    return Credentials.display_credentials() 

def main():
    print("Hello There,welcome to password locker.what`s your name?")

    user_name = input()   
    print (f"welcome {user_name}, what would you like to do today?")
    print('\n')

    while True:
        print("please choose: ca- to create an account,cc -to create credentials, li-to log in to your account,dc -to displaycredentials, ex-to exit")
        user_reply=input().lower()

        if user_reply == 'ca':
            print("New Account")
            print("*"*100)

            print("Enter User Name...")   
            userName =input()

            print("Your password...") 
            userPassword =input()

            save_password(create_password(userName,userPassword))
            print('\n')
            print(f"Your new account:user name is {userName} and the password is {userPassword}")
            print('\n')

        elif user_reply == 'cc':
            print("create a new credential for account")
            print("*"*100)

            print("Your User name....")
            userName =input()

            print("Social Accout...")
            account =input()

            while True:

                 print("*"*50)
                 print("choose an option to set a password: ep-enter a password ,gp-generate a password, ex-exit")
                 Password_code = input('Enter the chosen option...')
                 print("*"*50)
                 if Password_code =='ep':
                      print(" ")
                      userPassword =input("Enter your password.....")
                      break
                 elif Password_code =='gp':
                     userPassword = generate_password()
                     break 
                 elif  Password_code =='ex': 
                     break
                 else:
                     print("Please try again buddy")   
               
            save_credentials(create_credentials(user_name, account,userPassword))  
            print('\n')
            print(f"The New credentials for {user_name} ,*{account}* account and the username for the account is *{user_name}* password **{userPassword}**")
            print('\n')

        elif user_reply =='li':
            print("-"*50) 
            print(' ') 
            print(f'please fill in your login details')
            print('Your username is....')
            user_name = input()

            print("password....")
            userPassword = input()

            for password in Password. password_list:
                if password==userPassword:
                    print("You already registered buddy")
                else:
                    print("You already logged in to your account")
                    break

                print('\n') 

        elif user_reply =='dc':
            print(' ')
            if display_credentials():
                print("This is your credentials list:") .lower().strip()
                print(' ')
                for credentials in display_credentials():
                    # print(f"Social Account:{credentials.account,Password:{credentials.userPassword")
                 print('')  
            else:
                print('')
                print('No credentials are saved')
                print('')
        elif user_reply =='ex':
            print('thanks for visiting us!') 
            break
        else:
            print('enter user codes as displayed please!')              

                    
if __name__ == '__main__':
    main()
