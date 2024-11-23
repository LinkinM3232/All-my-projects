
#1 задание
film = {
    "Название": "Веномчик 3",
    "Год": 2024,
    "Жанр": "Боевичок"
}
print(film)


#2 задание
name = input("ВВЕДИТЕ ИМЯ: ")
age = input("ВВЕДИТЕ ВОЗРАСТ: ")
dict =  {}
dict[name] = age
print(dict)
name = input("ВВЕДИТЕ ИМЯ: ")
age = input("ВВЕДИТЕ ВОЗРАСТ: ")
dict =  {}
dict[name] = age
print(dict)
name = input("ВВЕДИТЕ ИМЯ: ")
age = input("ВВЕДИТЕ ВОЗРАСТ: ")
dict =  {}
dict[name] = age
print(dict)

#3 задание
grades = {"математика": 5, "физика": -6, "информатика": 666, "химия": 52}
average_grade = sum(grades.values()) / len(grades)
print(f"Средний балл: {average_grade}")
best_subject = max(grades.items(), key=lambda item: item[1])[0]
print(f"Лучшая оценка по предмету: {best_subject}")


#4 задание
text = input("Введите строку: ")
words = text.lower().split()
word_counts = {}
for word in words:
  word_counts[word] = word_counts.get(word, 0) + 1
print("\nСловарь подсчета слов:")
for word, count in word_counts.items():
  print(f"{word}: {count}")



#5 задание
products = {}
for i in range(3):
    name = input(f"Введите название продукта {i + 1}: ")
    while True:
        try:
            price = int(input(f"Введите его стоимость: "))
            if price >= 0:
                products[name] = price
                break
            else:
                print("Стоимость должна быть неотрицательной.")
        except ValueError:
            print("Некорректный ввод стоимости. Пожалуйста, введите целое число.")
requested_product = input("Какой продукт вы хотите купить? ")
price = products.get(requested_product)
if price is not None:
    print(f"Стоимость {requested_product}: {price}")
else:
    print(f"Извините, продукта {requested_product} нет в наличии.")



#6 задание
    employees = {}
    def add_employee(emp_id, name, position, salary):
        employees[emp_id] = {"имя": name, "должность": position, "зарплата": salary}
    def display_employees():
        for emp_id, info in employees.items():
            print(f"ID: {emp_id}, Имя: {info['имя']}, Должность: {info['должность']}, Зарплата: {info['зарплата']}")
    def find_employee(emp_id):
        return employees.get(emp_id, "Сотрудник не найден")
    def update_salary(emp_id, new_salary):
        if emp_id in employees:
            employees[emp_id]['зарплата'] = new_salary
        else:
            print("Сотрудник не найден")
    def delete_employee(emp_id):
        if emp_id in employees:
            del employees[emp_id]
        else:
            print("Сотрудник не найден")