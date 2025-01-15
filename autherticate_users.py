"""Create a simple authertication system where users loggend in with their stored username and password"""
"""from pickle import FALSE

from django.contrib.auth import authenticate"""
def authenticate(username, password):
    if (username == "farooq" and password == "password123"):
        return True
    else:
        return False

"""Main Program"""
username = input("Please enter your Username: ")
password = input("Enter your password: ")
if authenticate(username, password):
    print("Login Successful")
else:
    print("Login Failed. Please try again")