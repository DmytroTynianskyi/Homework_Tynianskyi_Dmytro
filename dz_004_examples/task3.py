# Завдання 3
# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
# Конструктор має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із клавіатури.
# Виведіть усіх співробітників, які були прийняті після цього року.

class Employee:
    def __init__(self, first_name, last_name, department, year):
        if not first_name or not last_name or not department or year < 1900:
            raise ValueError("Invalid employee data")
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.year = year


def get_employees_after_year(year, employees):
    result = []
    for emp in employees:
        if emp.year > year:
            result.append(emp)
    return result


employees = []
try:
    n = int(input("Enter number of employees: "))
    for _ in range(n):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        department = input("Enter department: ")
        year = int(input("Enter year of employment: "))
        employees.append(Employee(first_name, last_name, department, year))

    filter_year = int(input("Enter year to filter employees: "))
    filtered_employees = get_employees_after_year(filter_year, employees)

    print(f"Employees hired after {filter_year}:")
    for emp in filtered_employees:
        print(f"{emp.first_name} {emp.last_name}, Department: {emp.department}, Year: {emp.year}")
except ValueError as e:
    print(f"Error: {e}")
