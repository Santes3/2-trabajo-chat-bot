import requests
import os

#funcion para la solicitud de api para imagenes de patos
def get_duck_image():
    url = 'https://random-d.uk/api/random'
    res =  requests.get(url)
    data = res.json()
    return data['url']