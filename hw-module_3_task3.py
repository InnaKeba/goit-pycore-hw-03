#Завдання 3. Нормалізація телефонних номерів для SMS-розсилки
import re
def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^+\d]", "", phone_number.strip())
    if cleaned_number.startswith("+380"):
        return cleaned_number
    if cleaned_number.startswith("380"):
        return "+" + cleaned_number
    return "+38" + cleaned_number
raw_phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "(095) 234-5678\n",
    "38050 111 22 11   "]
sanitized_numbers = [normalize_phone(num) for num in raw_phone_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



"""
Критерії оцінювання:
Коректність роботи функції: функція має правильно обробляти різні формати номерів,
враховуючи наявність або відсутність міжнародного коду. - done (функція normalize_phone)
Читабельність коду: код має бути чистим, добре організованим і добре документованим.
Правильне використання регулярних виразів для видалення зайвих символів та форматування номера.
"""