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


# For the chest workout
def chest():
    #This is to retrive the excercise based on the type chosen
    chest_excercises = session.query(Excercises).filter(Excercises.type == 'Chest').all()
    print(chest_excercises)
    
    #To be able to chose the excercise
    quitting = False
    chest_options = ["Return", "Not feeling it"]
    chest_menu = TerminalMenu(chest_options)

    while quitting == False:
        index = chest_menu.show()
        index_choice = chest_options[index]
 
        if index_choice == 'Nah not feeling it':
            exit()
        elif index_choice == 'Return':
            quitting = True


#This will be to begin working out
def start_workout(usr):

    
    quitting = False
    options = ["Chest", "Lats", "Triceps", "Bicep", "Quadriceps", "Hamstrings", "View Stats","Return" ,"Nah not feeling it"]
    start_menu = TerminalMenu(options)

    while quitting == False:
        optionsIndex = start_menu.show()
        optionsChoice = options[optionsIndex]
        if optionsChoice == "Chest":
            chest()
        elif optionsChoice == "Lats":
            pass
        elif optionsChoice == "Triceps":
            pass
        elif optionsChoice == "Bicep":
            pass
        elif optionsChoice == "Quadriceps":
            pass
        elif optionsChoice == "Hamstrings":    
            pass
        elif optionsChoice == 'Nah not feeling it':
            exit()
        elif optionsChoice == "View Stats":
            stats(usr)
        elif optionsChoice == 'Return':
            quitting = True



#This is for whenever people want to view stats
def stats(usr):
    user = session.query(User).filter(User.username == usr).first()

    print(f"Chest: { user.stats[0].chest}")
    print(f"Hamstrings: { user.stats[0].hamstrings}")
    print(f"Lats: { user.stats[0].lats}")
    print(f"Triceps: { user.stats[0].triceps}")
    print(f"Biceps: { user.stats[0].biceps}")
    print(f"Abdominals: { user.stats[0].abdominals}")
    print(f"Quadriceps: { user.stats[0].quadriceps}")
    #Got to have the stats of the username that is logged in 
    


#This works on if the user chose to click Sign up
def sign_up():
    all_usernames=session.query(User.username).all()
   
    #Retrieve the Users information
    firstname = input("First Name:")
    lastname = input("Last Name:")

    #This checks to see if the username is in the system
    user_name = input("Username:")

    #iterate over the username
    if all_usernames == []:
        pass
    else:
        if any([ user_name in i for i in all_usernames]):
            print("Sorry, to slow name was already taken!!!")
            user_name = input("Username:")
        else:
            pass
        
    new_stats = Stats( 
        chest = 0,
        lats = 0,
        triceps = 0,
        biceps = 0,
        abdominals = 0,
        quadriceps = 0,
        hamstrings = 0
    )
    new_user = User(
        first_name = firstname,
        last_name = lastname,
        username = user_name,
    )
 
    #Takes all the information and sends it to the table 
    session.add_all([new_user, new_stats])
    session.commit()

    #Retrieve the user just created and then give them new stats
    user_stats = session.query(User).filter(User.username == user_name).first()
    user_stats.stats.append(new_stats)
    session.commit()


    #The second menu after creating your user
    quitting = False
    options = [f"Ready to get ripped {user_name}","View Stats","Return" ,"Nah not feeling it"]
    second_menu = TerminalMenu(options)

    while quitting == False:
        optionsIndex = second_menu.show()
        optionsChoice = options[optionsIndex]
        if optionsChoice == f"Ready to get ripped {user_name}":
            start_workout(user_name)
        elif(optionsChoice == 'Nah not feeling it'):
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

    user_name = input("Username:")
    #iterate over the username
    if all_usernames == []:    
        print("Need to Create an Account")
        sign_up()            
    else:
        if any([ user_name in i for i in all_usernames]):
            print(f"Welcome Back, {user_name}!!!")
            while quitting == False:
                optionsIndex = third_menu.show()
                optionsChoice = options[optionsIndex]
                if optionsChoice == "Start Getting Ripped":
                    start_workout(user_name)
                elif(optionsChoice == 'Nah not feeling it'):
                    exit()
                elif(optionsChoice == "View Stats"):
                    stats(user_name)
                elif(optionsChoice == 'Return'):
                    quitting = True
        else:
            print("Need to Create an Account")
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
    



