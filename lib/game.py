from simple_term_menu import TerminalMenu
from pyfiglet import Figlet
import requests
from decouple import config

#To be able to communicate with the database
engine = create_engine("sqlite:///gym.db")
Session = sessionmaker(bind=engine)
session = Session()


# Show to title of the CLI
figlet = Figlet(font='slant')
print(figlet.renderText("Gym Simulator"))




#Getting the CLI menu started
# options = ["Log In", "Sign Up", "Quit"]

# main_menu = TerminalMenu(options)

# quitting = False

# while quitting == False:
#     optionsIndex = main_menu.show()
#     optionsChoice = options[optionsIndex]

#     if(optionsChoice == 'Quit'):
#         quitting = True
#     else:
#         print(optionsChoice)


#