from simple_term_menu import TerminalMenu
from pyfiglet import Figlet
import requests
from decouple import config
from models import User, Stats, Excercises
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
import sqlite3

#To be able to communicate with the database
engine = create_engine('sqlite:///gym.db')
Session = sessionmaker(bind=engine)
session = Session()
# conn = sqlite3.connect('gym.db')
# cursor = conn.cursor()


#Global Varibles needed for the funcitons
quitting = False

# Show to title of the CLI
figlet = Figlet(font='slant')
print(figlet.renderText("Gym Simulator"))

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
        for n in all_usernames:
        if user_name == n[0]:
            print("Sorry, to slow name was already taken!!!")
        else:
            usr = False

    new_user = User(
        first_name = firstname,
        last_name = lastname,
        username = user_name
    )

    #Takes all the information and sends it to the table 
    # session.add(new_user)
    # session.commit()


    #The second menu after creating your user
    options = [f"Ready to get ripped {username}","View Stats", "Quit"]
    second_menu = TerminalMenu(options)

    while quitting == False:
        optionsIndex = second_menu.show()
        optionsChoice = 
        if 
    


    


#This is for if they choose log in
def log_in():
    print("log_in")

#To Start the Main Menu of the program
def menu():
    options = ["Log In", "Sign Up", "Quit"]

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
    



