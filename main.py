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

    # создаем словарь/массив объектов с координатами
    coords = [{'x': 100, 'y': 0}, {'x': 200, 'y': 0}, {'x': 300, 'y': 0}]

    # инициализируем переменную - флаг для выхода из бесконечного цикла
    isContinue = True

    # запускаем "рендер" цикл
    while isContinue:

        # перебираем точки из массива
        for point in coords:

            # вывод точек для отладки
            print(point)

            # задаем новые координаты текущей точки (увеличиваем X , Y)
            point['y'] = point['y'] + 50
            point['x'] = point['x'] + 50

            #рисуем точку (метод из либы)
            #draw()

        # после выполнения каждой итерации внешнего цикла проверяем Y координату любой точки, для остановки рендера
        # это условие зависит от конкретной задачи в ТЗ
        if point['y'] > 1000:
            # просваиваем переменной/флагу значение false, что бы прервать выполнение бесконечного цикла
            isContinue = False

# запуск функции
snow()



