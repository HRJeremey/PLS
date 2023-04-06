import sys
import os
import helpers.MainMenu as menu
from dataObjects.Catalog import Catalog
from dataObjects.Person import Person

global c
global options
global admin

admin = False
   
def MainMenu(clear = True):
    menu.PrintMenu(options, clear)
    
def LoginAction():
  #  os.system("cls")
    username = str(input("Enter  Username :")) 
    password = str(input("Enter  Password :")) 

    if Person.Login(username, password):
        if username == "admin":
            global admin
            admin = True            
        print("Successfully logged in!")
        #CONTINUE FUNCTION
        InitializeSystem()
    else:
        print("\nInvalid credentials!")        
        actions = {1 : {"Try Again?": LoginAction}, 2 : {"Back to menu" : MainMenu}}
        menu.PrintMenu(actions, False)

def SignOff():
    global options
    options = {1: {"Login": LoginAction}, 9:{"Exit": sys.exit}}
    MainMenu()

def InitializeSystem():
    global c 
    global options
    
    c = Catalog();
    
    if admin:
        options = c.AdminMenu();
    else:
        options = c.MemberMenu()
        
    options[8] = {"Sign off": SignOff}
    options[9] = {"Exit": sys.exit}
    
    MainMenu(False);

#MENU OPTIONS: 
options = {1: {"Login": LoginAction}, 9:{"Exit": sys.exit}}
while True:
    MainMenu(False)