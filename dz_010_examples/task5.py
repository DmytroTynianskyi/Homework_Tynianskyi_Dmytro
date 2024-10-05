# Завдання 5

# З клавіатури вводиться рядок, в якому є інформація про прізвище,
# ім'я, дату народження, електронну адресу та відгук про курси учня.
# Написати функцію, яка, використовуючи регулярні вирази, витягне дані з рядка і поверне словник.
import re


def extract_student_info(input_string):
    pattern = r'(?P<surname>[A-Za-z]+)\s+(?P<name>[A-Za-z]+)\s+(?P<dob>\d{1,2}/\d{1,2}/\d{4})\s+(?P<email>[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\s+(?P<feedback>.+)'
    match = re.match(pattern, input_string)

    if match:
        return match.groupdict()
    else:
        return None

input_string = "Smith John 15/05/1995 john.smith@example.com Great course!"
student_info = extract_student_info(input_string)
print(student_info)
