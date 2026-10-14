numbers = [1, 2, 3, 4, 5]


def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)


print(find_average(numbers=numbers)) # 3.0

'''не предусмотрена обработка ошибки - деления на ноль
ZeroDivisionError: division by zero
'''

#print(find_average(numbers=[])) # ZeroDivisionError: division by zero
try:
    print(find_average(numbers=[]))
except ZeroDivisionError:
    print("The list is empty")

print("we are wait here! Try to go through error")