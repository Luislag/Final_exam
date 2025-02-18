def days_since_birthday(birthday):
    parts = birthday.split('-')
    birth_year = int(parts[2])
    current_year = 2025
    total_days = 0
    for year in range(birth_year + 1, current_year):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            total_days += 366
        else:
            total_days += 365
    return total_days
print(days_since_birthday("30-07-2005"))