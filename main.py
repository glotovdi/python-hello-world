import requests
from requests.exceptions import HTTPError

def greetings(name):
    print(f'Здарова, {name}!')

def main():
    name = input("Введите имя \n")
    greetings(name)


def request():
    try:
        response = requests.get('https://api.github.com')
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')

request()

def snow():
    coords = [{'x': 100, 'y': 0}, {'x': 200, 'y': 0}, {'x': 300, 'y': 0}]

    isContinue = True

    while isContinue:
        for i in coords:
            i['y'] = i['y'] + 100
            #draw()
            print(i)
        if i['y'] > 1000:
            isContinue = False

snow()



