import requests
from datetime import datetime


PIXELA_USERNAME = "osegbeg"
PIXELA_TOKEN = "breadwinningmentality1"

create_user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

create_graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

create_graph_parameters = {
    "id": "codinghabit100",
    "name": "codingHabitGraph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

# response = requests.post(pixela_endpoint, json= create_user_params)
# print(response.text)

# response = requests.post(create_graph_endpoint, json= create_graph_parameters, headers= headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{create_graph_parameters["id"]}"

today = datetime.now()

post_pixel_parameters = {
    "date": "20241101",
    "quantity": input("how many minutes did you put in today? :"),
}

# put_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{create_graph_parameters["id"]}/20241101"
#
# put_pixel_parameters = {
#     "quantity": "211",
# }
response = requests.post(url=post_pixel_endpoint, json= post_pixel_parameters, headers=headers)

# response = requests.put(url=put_pixel_endpoint, json= put_pixel_parameters, headers=headers)
print(response.text)