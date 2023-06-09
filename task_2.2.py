# Задача 2.2
# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    if (month < 1 or month > 12):
        return -1
    if month != 0:
        month -= 1
    return month // 3 + 1

def print_quarter_of(month):
    print(f'Задан месяц {month}. ', end="")
    quarter = quarter_of(month)
    if quarter == -1:
        print('Неверное число месяца. Введите число от 1 до 12.')
    else:
        print(f'Номер квартала заданного месяца: {quarter}.')
        
for m in range(-2, 15):
    print_quarter_of(m)