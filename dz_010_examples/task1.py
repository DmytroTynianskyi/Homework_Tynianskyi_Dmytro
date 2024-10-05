# Завдання 1

# Написати функцію, яка за допомогою регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.

import re
from collections import Counter


def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    frequency = Counter(words)
    return frequency


text = "Hello world! Hello everyone. Welcome to the world of programming."
print(word_frequency(text))
