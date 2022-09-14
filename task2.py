'''
this is Selenium Web Driver Task by Babukhadia Levani.
'''

from pytest import* 

'''
to implement the scenario, we need to ask
users to input their credentials, such as, usernames and passwords.
for an user to log in, he/she must be already registered. 
So, we have a dictionary of registered users with their credentials; and if an user enters credentials
from the dictionary, she/she will login successfully otherwise not.
'''
class users:
    registered={"username1":123, "username2":1234, "username3":12345}
    # random users
class add_user:
    def __init__(self, username, passwrod):
        self.username=username
        self.passwrod=passwrod
    

    def adding(self,username,passwrod):
        users.registered+{username:passwrod}
            
choice=input("would you like to sign up before logging in? enter y if yes n otherwise: ")
if choice=="y":
    add_user.adding(input("enter username: "),input("enter password: "))

    
    
while True:
    my_username=input("enter your username: ")
    my_password=input("enter your password: ")

    if my_username in users.registered.keys() and my_password in users.registered.values():
        break
    else:
        print("Invalid username, enter your username and password again: ")




