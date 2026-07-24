#Code here
# Created by Grant Samson
#Creating a Python program that stimulates logging into a system. Set the default username and password to:
#username = "admin"
#password = "admin@2026"

username = "admin"
password = "admin@2026"

#setting keywords for what users should do when the specific things are displayed

user=input("Input your username ")
passw=input("input your password ")
# Here I set commands for what should be displayed when the password or username entered by the individual is incorrect

invalid=("password is incorrect")
incorrect=("username is incorrect")
# Set my commands for what should happen when the username and password match, and when it doesn't match with the default username and password, what should be displayed if it is incorrect
if username == user and password == passw:
    print("You have successfully logged in")
elif ( username != user and password != passw):
    print(invalid)
    print(incorrect)
elif (username == user and password != passw):
    print(incorrect)
else:
    print(invalid)
