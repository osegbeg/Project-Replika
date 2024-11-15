import requests
import os
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
now = datetime.now()

GENDER = "MALE"
WEIGHT_KG = 65
HEIGHT_CM = 165
AGE = 29

# NLM means Natural Language Model
nlm_host = "https://trackapi.nutritionix.com"
nlm_exercise_endpoint = f"{nlm_host}/v2/natural/exercise"

sheety_host = "https://api.sheety.co"
sheety_endpoint = "https://api.sheety.co/5fde37c3a9f9fba94f4e8b51630fc39f/myMindWorkouts/workouts"
sheety_headers = {
    "Authorization": "Bearer BearerAuthentication"
}

nlm_headers = {
    "x-app-id": os.getenv("NLM_APP_ID"),
    "x-app-key": os.getenv("NLM_APP_KEY")
}

nlm_request_parameters = {
    "query" : str(input("Tell me which exercises you did: ")),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


nlm_response = requests.post(url=nlm_exercise_endpoint, json=nlm_request_parameters, headers=nlm_headers)
if nlm_response.status_code != 200:
    print(f"Error with NLM request: {nlm_response.text}")
    exit()

# sheety_response = requests.get(url=sheety_endpoint, headers=sheety_headers) #Debugging line
#print(sheety_response.text) #Debugging line
exercise_data = nlm_response.json()
# print("NLM Response Data:", exercise_data) ##Debugging line
for exercise in exercise_data["exercises"]:
    workouts = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_post = requests.post(url=sheety_endpoint, json=workouts, headers=sheety_headers)
    print(sheety_post.text)
