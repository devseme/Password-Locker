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
            print()
