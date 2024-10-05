# Завдання 1

# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел.
# Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.

import random

with open("random_numbers.txt", "w") as file:
    for _ in range(10000):
        number = random.uniform(0, 100) 
        file.write(f"{number}\n") 

with open("random_numbers.txt", "r") as file:
    numbers = file.readlines()  

numbers = [float(number.strip()) for number in numbers]
total_sum = sum(numbers)

print(f"Сума чисел: {total_sum}")
