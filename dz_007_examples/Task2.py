# Завдання 2

# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл


# Варіант 1: Генератор

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares_gen = (x**2 for x in numbers if x % 2 == 0)

for square in squares_gen:
    print(square)
    
    
    
# Варіант 2: Цикл

squares_list = []
for x in numbers:
    if x % 2 == 0:
        squares_list.append(x**2)

print(squares_list)
