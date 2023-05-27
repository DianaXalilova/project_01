# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    digits_dict = {0: 'Zero' , 
                   1: 'One', 
                   2: 'Two',
                   3: 'Three',
                   4: 'Four',
                   5: 'Five',
                   6: 'Six',
                   7: 'Seven',
                   8: 'Eight',
                   9: 'Nine'}
    return digits_dict.get(number)

for digit in range(0, 11):
    print(f'Задано число {digit}. ', end="")
    result = switch_it_up(digit)
    if result:
        print(f'Произносится {result}.')
    else:
        print('Нет такого значения.')