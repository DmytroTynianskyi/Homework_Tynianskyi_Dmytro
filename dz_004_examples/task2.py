# Завдання 2

# Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення,
# ділення та піднесення до ступеня. Програма має видавати повідомлення про помилку та продовжувати
# роботу під час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input(
                "Enter the operation (+, -, *, /, ** or 'exit' to quit): ")

            if operation == 'exit':
                print("Exiting the calculator.")
                break

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero!")
                result = num1 / num2
            elif operation == '**':
                if num1 == 0 and num2 < 0:
                    raise ValueError(
                        "Zero cannot be raised to a negative power!")
                result = num1 ** num2
            else:
                raise ValueError("Invalid operation!")

            print(f"Result: {result}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")


calculator()
