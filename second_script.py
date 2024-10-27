import re

#1 задание
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$'
    return bool(re.match(pattern, email))

# Примеры использования
print(is_valid_email("example@test.com"))
print(is_valid_email("example@com"))

#2 задание
def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-\s]?\d{3}-\d{4}'
    return re.findall(pattern, text)

print(extract_phone_numbers("Мой номер (666) 952-4444 and 123-456-7890."))

#3 задание
def replace_dates(text):
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    return re.sub(pattern, r'\3-\2-\1', text)

print(replace_dates("Сегодня 01/01/3002"))

#4 задание
def remove_duplicate_words(text):
    pattern = r'\b(\w+)\b(?:\s+\1\b)+'
    return re.sub(pattern, r'\1', text)

print(remove_duplicate_words("привет привет ахахвадхдащвлащушао4885445545"))

#5 задание

def extract_hashtags(text):
    pattern = r'#(\w+)'
    return re.findall(pattern, text)

print(extract_hashtags("#ввов #ззовв #ЧИВО"))


