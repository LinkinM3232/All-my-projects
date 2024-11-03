import re
#1 задание
def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.(com|org|ru)$'
    return bool(re.match(pattern, email))
print(is_valid_email("example.email@gmail.com"))
print(is_valid_email("wrong_email@domain"))
print(is_valid_email("user_name@domain.org"))


#2 задание
def replace_prices(text: str) -> str:
    pattern = r'\b\d+\s*руб\w*'
    return re.sub(pattern, 'PRICE', text)

text = "Цена ноутбука 55656 руб., а айфона - 1 рубль."
print(replace_prices(text))

#3 задание
def split_by_sentence(text: str) -> list:
    pattern = r'(?<=[.!?…])\s+'
    return re.split(pattern, text)

text = "Привет! Как дела? Все хорошо..."
print(split_by_sentence(text))

#4 задание
def extract_hashtags(text: str) -> list:
    pattern = r'#\w+'
    return re.findall(pattern, text)

text = "Сегодня отличный день! #python #programming #100DaysOfCode"
print(extract_hashtags(text))

#5 задание
def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@#$%&*]', password):
        return False
    return True

print(is_strong_password("Passw0rd@"))
print(is_strong_password("weakpass"))







