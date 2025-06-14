#Завдання 1
#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
from datetime import datetime
def get_days_from_today(date):
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = (parsed_date - today).days
        return difference
    except ValueError:
        return"Помилка: Невірний формат дати. Використовуйте формат'РРРР-ММ-ДД'."
print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-06-01"))
print(get_days_from_today("21-10-09")) #Перевірка except
print(get_days_from_today("2021/01/09")) #Перевірка except


"""Критерії оцінювання:
Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами. - done (перевірка difference)
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних. - done (перевірка except) Додано return для помилки
Читабельність коду: код повинен бути чистим і добре документованим."""