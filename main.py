from first_script import wqw, program, стоимость_разговора, ttt, count_same_digits, count_different_digits, \
    remove_digits

number = int(input("Введите число от 1 до 100: "))
wqw(number)

number = float(input("Введите число: "))
degree = int(input("Введите степень от 0 до 7: "))
program(number, degree)

operator = input("Введите оператора: ")
стоимость_разговора(operator)

x = int(input("Введите x: "))
y= int(input("Введите y: "))

result = x ** y
print(f"{x} в степени {y} равно {result}")
ttt(x, y)

result = count_same_digits()
print(f"Количествоо чисел с двумя одинаковыми знаками равно: {result}")

result = count_different_digits()
print(f"Количество с разными знаками: {result}")

number = input("Введите целоееп число: ")
result = remove_digits(number)
print(f"число итоговое: {result}")









