# Завдання 3

# Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку(аналог reversed).

class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.lst[self.index]
        self.index -= 1
        return value

lst = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(lst)

for item in reverse_iter:
    print(item)
