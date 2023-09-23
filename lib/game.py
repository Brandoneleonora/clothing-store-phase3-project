from simple_term_menu import TerminalMenu
from pyfiglet import Figlet
import requests
from decouple import config
from models import User, Stats, Excercises
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
import sys, subprocess

#To be able to communicate with the database
engine = create_engine('sqlite:///gym.db')
Session = sessionmaker(bind=engine)
session = Session()



# Show to title of the CLI
figlet = Figlet(font='slant')
print(figlet.renderText("Gym Simulator"))





#This will be to begin working out
def start_workout():
    quitting = False
    options = ["Chest", "Back", "Triceps", "Bicep", "Quadriceps", "Hamstrings","Start Getting Ripped", "View Stats","Return" ,"Nah not feeling it"]
    third_menu = TerminalMenu(options)
    usr = True

    while usr == True:
        user_name = input("Username:")
        #iterate over the username
        for n in all_usernames:
            if user_name == n[0]:
                print(f"Welcome Back, {user_name}!!!")
                while quitting == False:
                    optionsIndex = third_menu.show()
                    optionsChoice = options[optionsIndex]
                    if(optionsChoice == 'Nah not feeling it'):
                        exit()
                    elif(optionsChoice == "View Stats"):
                        stats(user_name)
                    elif(optionsChoice == 'Return'):
                        quitting = True
                        usr = False
            else:
                usr = False
                print("Need an Account")
                sign_up()




#This is for whenever people want to view stats
def stats(usr):
    user = session.query(User).filter(User.username == usr).first()

    print(user.stats)

    new_stats = 
        chest = 0,
        lats = 0,
        triceps = 0,
        biceps = 0,
        abdominals = 0,
        quadriceps = 0,
        hangstrings = 0

    print(new_stats)
    #Got to have the stats of the username that is logged in 
    


#This works on if the user chose to click Sign up
def sign_up():
    all_usernames=session.query(User.username).all()

    #Retrieve the Users information
    firstname = input("First Name:")
    lastname = input("Last Name:")

    #This checks to see if the username is in the system
    usr = True

    while usr == True:

        user_name = input("Username:")
        #iterate over the username
        if all_usernames == []:
            usr = False
        else:
            for n in all_usernames:
                if user_name == n[0]:
                    print("Sorry, to slow name was already taken!!!")
                elif n == []:
                    usr = False
                else:
                    usr = False

        
    new_user = User(
        first_name = firstname,
        last_name = lastname,
        username = user_name,
        stats =
    )
 
    #Takes all the information and sends it to the table 
    session.add(new_user)
    session.commit()


    #The second menu after creating your user
    quitting = False
    options = [f"Ready to get ripped {user_name}","View Stats","Return" ,"Nah not feeling it"]
    second_menu = TerminalMenu(options)

    while quitting == False:
        optionsIndex = second_menu.show()
        optionsChoice = options[optionsIndex]
        if(optionsChoice == 'Nah not feeling it'):
            exit()
        elif(optionsChoice == "View Stats"):
            stats(user_name)
        elif(optionsChoice == 'Return'):
            quitting = True
    


    


#This is for if they choose log in
def log_in():
    all_usernames=session.query(User.username).all()
    quitting = False
    options = ["Start Getting Ripped", "View Stats","Return" ,"Nah not feeling it"]
    third_menu = TerminalMenu(options)
    usr = True

    while usr == True:
        user_name = input("Username:")
        #iterate over the username
        if all_usernames == []:
            usr = False
            print("Need to Create an Account")
            sign_up()            
        else:
            for n in all_usernames:
                if user_name == n[0]:
                    print(f"Welcome Back, {user_name}!!!")
                    while quitting == False:
                        optionsIndex = third_menu.show()
                        optionsChoice = options[optionsIndex]
                        if(optionsChoice == 'Nah not feeling it'):
                            exit()
                        elif(optionsChoice == "View Stats"):
                            stats(user_name)
                        elif(optionsChoice == 'Return'):
                            quitting = True
                            usr = False
                else:
                    usr = False
                    print("Need an Account")
                    sign_up()




#To Start the Main Menu of the program
def menu():
    options = ["Log In", "Sign Up", "Quit"]
    quitting = False
    main_menu = TerminalMenu(options)

    while quitting == False:
        optionsIndex = main_menu.show()
        optionsChoice = options[optionsIndex]

        if(optionsChoice == 'Quit'):
            quitting = True
        elif(optionsChoice == 'Sign Up'):
            sign_up()
        else:
            log_in()





#Getting the CLI menu started
if __name__ == '__main__':
    menu()
    



