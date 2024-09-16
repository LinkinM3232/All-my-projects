#1 задание
def wqw(number):
    if number < 1 or number > 100:
        print("Ошибка")
    elif number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

#2 задание
def program(number, degree):
    if 0 <= degree <= 7:
        chivo = number ** degree
        print(f"{number} в степени {degree} равно {chivo}")
    else:
        print("Ошибка")

#3 задание
def стоимость_разговора(operator):
    cost_per_minute = float(input("Введите стоимость разговора: "))
    print(f"Оператор: {operator}, стоимость разговора: {cost_per_minute} руб ")



