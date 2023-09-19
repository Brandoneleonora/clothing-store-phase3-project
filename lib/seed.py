from models import Excercises
from decouple import config
import requests
import json
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

# To be able to send to communicate with database
engine = create_engine("sqlite:///gym.db")
Session = sessionmaker(bind=engine)
session = Session()

#API for excercises
muscles = ["biceps", "chest", "legs", "core", "back", "triceps"]

#Search for the muscle I want from the API then puts all the workouts in the table
for m in muscles:
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(m)
    response = requests.get(api_url, headers={'X-Api-Key': config("API_KEY")})
    json_data = json.loads(response.text)
    for js in json_data:
        excercise = Excercises(
            type = js['muscle'],
            name = js['name'],
            instructions = js["instructions"]
        )

        session.add(excercise)
        session.commit()

import ipdb; ipdb.set_trace()