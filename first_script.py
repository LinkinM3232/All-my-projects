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


#1 задание. Модуль 3. Циклы. Часть 3
def ttt(x, y):
    return x ** y

#2 задание. Модуль 3. Циклы. Часть 3
def count_same_digits():
    count = 0
    for number in range(100, 1000):
        str_number = str(number)
        if str_number[0] == str_number[1] or str_number[1] == str_number[2] or str_number[0] == str_number[2]:
            count += 1
        return count
#3 задание. Модуль 3. Циклы. Часть 3
def count_different_digits():
    count = 0
    for number in range(100, 10000):
        str_number = str(number)
        if len(set(str_number)) == len(str_number):
            count += 1
    return count

#4 задание. Модуль 3. Циклы. Часть 3
def remove_digits(number):
    return number.replace("3", " ").replace("6"," ")


#1 задание. Модуль 4. Строки. Списки. Часть 1
pervoayastrochka = input("Введите строку: ")
pervoayastrochka = pervoayastrochka.replace(" ", "").lower()

if pervoayastrochka == pervoayastrochka[::-1]:
    print("Это палиндром сто проц")
else:
    print("Не палиндром хз что это")

#2 задание. Модуль 4. Строки. Списки. Часть 1
AAAETOCHTOTEXT = input("Введите текст: ")
reservNIEE_SLOVA = input("Введите зарезервированные слова: ").split()

SLOVA = AAAETOCHTOTEXT.split()

for i in range(len(SLOVA)):
    if SLOVA[i].lower() in reservNIEE_SLOVA:
        SLOVA[i] = SLOVA[i].upper()

izmenenny_tekst = " ".join(SLOVA)
print("Измененный текст:", izmenenny_tekst)

#3 задание. Модуль 4. Строки. Списки. Часть 1
AAAETOCHTOTEXT = input("Введите текст: ")
AAAETOCHTOTEXT = AAAETOCHTOTEXT.count('.') + AAAETOCHTOTEXT.count('!') + AAAETOCHTOTEXT.count('?')
print("Количество предложений:", AAAETOCHTOTEXT)










