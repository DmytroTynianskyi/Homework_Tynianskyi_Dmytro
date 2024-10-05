# Завдання 2

# Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про дату народження,
# телефон та електронну адресу. Дані потрібно записати до іншого файлу.

import re


def extract_contact_info(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    date_of_birth_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
    phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'  
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    dates_of_birth = re.findall(date_of_birth_pattern, text)
    phones = re.findall(phone_pattern, text)
    emails = re.findall(email_pattern, text)

    with open(output_file, 'w') as file:
        for dob in dates_of_birth:
            file.write(f'Date of Birth: {dob}\n')
        for phone in phones:
            file.write(f'Phone: {phone}\n')
        for email in emails:
            file.write(f'Email: {email}\n')

# Приклад використання
# extract_contact_info('input.txt', 'output.txt')
