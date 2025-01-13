import requests
import json
import pandas as pd
from datetime import datetime


def post_token(username, password):
    url = f"https://drebalbi.pythonanywhere.com/api/v1/authentication/token/"
    headers = {"Content-Type": "application/json"}
    data = {"username": username, "password": password}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        dados = response.json()
        # print(f"Token: {dados['access']}")

    else:
        print(f"Erro ao obter o token: {response.status_code}")

    return response


def get(url, username, password):
    token = post_token(username, password).json()["access"]
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response


url = "https://drebalbi.pythonanywhere.com/api/v1/actors/"
username = "lixo01"
password = "@1215354Xl"


response = get(url, username, password)
data = response.json()
df = pd.DataFrame(data).set_index("id")
