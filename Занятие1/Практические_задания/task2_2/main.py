# x = сумм(1,2)
# x= сумм (1, макс (2,3))
length = int(input("Длина: "))
# 1 вызов функции input с входным аргументом "Длина:"
# 1.1 функция input ожидает ввода с клавиатуры
# 1.2 при нажатии Enter функция  input возвращает введенную строку
# 2 вызов функции int. на вход функции int передается возвращаемое значение функции input
# 3 присвоение переменной lenght возвращаемого значения функции int

width = int(input("Ширина: "))  # TODO привести к целочисленному типу данных

perimeter = length*2 + width*2  # TODO посчитать периметр прямоугольника

print(perimeter)
