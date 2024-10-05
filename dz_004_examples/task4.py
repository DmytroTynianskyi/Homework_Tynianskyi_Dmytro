# Завдання 4
# Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток,
# якщо користувач введе певне значення, і перехопіть цей виняток під час виклику функції.

class CustomException(Exception):
    def __init__(self, message="Custom exception triggered"):
        self.message = message
        super().__init__(self.message)


def check_value(value):
    if value == 13:
        raise CustomException("You entered 13, which is not allowed!")


try:
    user_input = int(input("Enter a number: "))
    check_value(user_input)
except CustomException as ce:
    print(f"Error: {ce}")
