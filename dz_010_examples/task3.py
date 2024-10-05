# Завдання 3

# Користувач вводить з клавіатури пропозицію. Написати функцію, яка друкуватиме на екран останні 3 символи кожного слова.

def print_last_three_chars(sentence):
    words = sentence.split()
    for word in words:
        print(word[-3:])  


user_input = input("Enter a sentence: ")
print_last_three_chars(user_input)
