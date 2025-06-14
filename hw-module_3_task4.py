#Завдання 4 привітань колег з днем народження. 
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    bd_date = today + timedelta(days=7)
    get_upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y-%m-%d').date()
        birthday_this_year = birthday.replace(year=today.year)
        if  birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        if today <= birthday_this_year <= bd_date:
            if birthday_this_year.weekday() in[5,6] or birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            get_upcoming_birthdays.append({'name': user['name'],'birthday': birthday_this_year.strftime('%Y-%m-%d')})
    return get_upcoming_birthdays

users = [{"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}]
get_upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні: ", get_upcoming_birthdays)