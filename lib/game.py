from simple_term_menu import TerminalMenu
from pyfiglet import Figlet
import requests
from decouple import config
from models import User, Stats, Excercises
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

#To be able to communicate with the database
engine = create_engine('sqlite:///gym.db')
Session = sessionmaker(bind=engine)
session = Session()


# Show to title of the CLI
figlet = Figlet(font='slant')
print(figlet.renderText("Gym Simulator"))

#This works on if the user chose to click Sign up
def sign_up():
    print("sign_up")

#This is for if they choose log in
def log_in():
    print("log_in")

#To Start the Main Menu of the program
def menu():
    options = ["Log In", "Sign Up", "Quit"]

    main_menu = TerminalMenu(options)
    quitting = False

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
    



