#1 задание
def sort_by_score(students):
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    return sorted_students
students = [("Алексей", 78), ("Мария", 92), ("Иван", 88), ("Екатерина", 95)]
result = sort_by_score(students)
print(result)

#2 задание
def min_elements(tuple1, tuple2):
    result = tuple(min(a, b) for a, b in zip(tuple1, tuple2))
    return result
tuple1 = (5, 10, 15)
tuple2 = (3, 12, 8)
result = min_elements(tuple1, tuple2)
print(result)


#3 задание
def count_unique(numbers):
    unique_count = len(set(numbers))
    return unique_count
numbers = (1, 2, 2, 3, 4, 4, 4, 5)
result = count_unique(numbers)
print("Количество уникальных элементов:", result)

#4 задание
def filter_even(numbers):
    even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers
numbers = (1, 2, 3, 4, 5, 6)
result = filter_even(numbers)
print(result)

#5 задание
def sum_of_squares(numbers):
    squares = tuple(x**2 for x in numbers)
    total = sum(squares)
    return squares, total
numbers = (1, 2, 3, 4)
squares, total = sum_of_squares(numbers)
print("Новый кортеж:", squares)
print("Сумма:", total)




