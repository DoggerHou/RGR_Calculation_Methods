import numpy as np
from prettytable import PrettyTable


#Вычисляем значение функции
def f(x):
    return np.log(x)


#Тело программы
a = 1                                   # Левая граница
b = 2                                   # Правая граица
n = 1                                   # Количество интервалов разбиений
td = ['n', 'Jh']                        # Список для вывода результатов в таблице
table = PrettyTable(td)
while n <= 20000000:
    h = (b - a) / n                     # Находим длину интервала
    J = 0.0                             # Значение интеграла
    x = [a + h * i for i in range(0, n+1)]
    for i in range (1, n):
        J += h * f(x[i])
    table.add_row([n, J])
    n *= 2

table.align = 'l'                       # Указываем выравнивание по левому краю
print(table)                            # Выводим таблицу
