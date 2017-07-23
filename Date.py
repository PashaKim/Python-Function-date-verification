
def is_year_leap(year):

    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False

def date(d,m,year):
    d_in_m = { 1: 31,
               2: 29 if is_year_leap(year) else 28,
               3: 31,
               4: 30,
               5: 31,
               6: 30,
               7: 31,
               8: 31,
               9: 30,
               10: 31,
               11: 30,
               12: 31}

    if 1 <= m <= 12 and 1 <= d <= d_in_m[m]:
        return True
    return False
print('Введите дату: день/месяц/год')
d=int(input('День: '))
m=int(input('Месяц: '))
year=int(input('Год: '))
if date(d,m,year)==True:
    print(d,'/',m,'/',year)
else:
    print('Неверная дата')
            
