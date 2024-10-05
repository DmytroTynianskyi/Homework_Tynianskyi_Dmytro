# Завдання 1

# Напишіть генератор, який повертає елементи заданого списку у зворотному порядку(аналог reversed).

def reverse_generator(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

my_list = [1, 2, 3, 4, 5]
for item in reverse_generator(my_list):
    print(item)
