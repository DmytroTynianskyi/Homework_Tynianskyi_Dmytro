# Завдання 4

# Напишіть функцію, яка буде аналізувати текст, що надходить до неї,
# і виводити тільки унікальні слова на екран, загальну кількість слів і кількість унікальних слів.
import re

def unique_word_analysis(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    total_words = len(words)
    unique_count = len(unique_words)

    print(f"Unique words: {unique_words}")
    print(f"Total words: {total_words}")
    print(f"Unique count: {unique_count}")


# Приклад використання
text = "Hello world! Hello everyone. Welcome to the world of programming."
unique_word_analysis(text)
