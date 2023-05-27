# Задача 2.1
# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    arr = sort(arr)
    return arr[0]

def maximum(arr):
    arr = sort(arr)
    return arr[-1]

def print_max_and_min(arr):
    print(f'max = {maximum(arr)}, min = {minimum(arr)}')

def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j] > key and j >= 0:
           arr[j + 1] = arr[j]
           j -= 1
        arr[j + 1] = key
    return arr

arr1 = [4,6,2,1,9,63,-134,566]         
arr2 = [-52, 56, 30, 29, -54, 0, -110] 
arr3 = [42, 54, 65, 87, 0]             
arr4 = [5]                             

print_max_and_min(arr1)
print_max_and_min(arr2)
print_max_and_min(arr3)
print_max_and_min(arr4)