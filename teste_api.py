'''importar uma biblioteca requests para fazer as requisições'''
import requests

'''endereço da API - A variável response guarda a resposta da requisição'''
URL = 'https://api.adviceslip.com/advice'

try:
    response = requests.get(URL)
    print(response.status_code)
    print(response.json())
    print(response.json()['slip'])
    print(response.json()['slip']['advice'])

except Exception as e:
    print(e)


