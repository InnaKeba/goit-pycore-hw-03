import random
def get_numbers_ticket(min_number, max_number, quantity):
    if (not isinstance(min_number, int) or
        not isinstance(max_number, int) or
        not isinstance(quantity, int)):
        return []
    if not (1 <= min_number <= max_number <= 1000 and 1 <= quantity <= (max_number - min_number + 1)):
        return []
    lottery_numbers = random.sample(range(min_number, max_number + 1), quantity)
    return sorted(lottery_numbers)

print(f"Ваші лотерейні числа: {get_numbers_ticket(1, 49, 5)}", )

""" Критерії оцінювання:
Валідність вхідних даних: функція повинна перевіряти коректність параметрів. - done (перевірка if)
Унікальність результату: усі числа у видачі повинні бути унікальними. - done (використання randome)
Відповідність вимогам: результат має бути у вигляді відсортованого списку. - done (використання sorted)
Читабельність коду: код має бути чистим і добре документованим. """
