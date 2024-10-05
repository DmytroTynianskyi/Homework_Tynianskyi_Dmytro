# Завдання 2

# Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так,
# щоб він зберігав базу посилань на диску і не «забув» при перезапуску.

import json
import os


class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.load_data()

    def load_data(self):
        if os.path.exists('links.json'):
            with open('links.json', 'r') as file:
                self.url_mapping = json.load(file)

    def save_data(self):
        with open('links.json', 'w') as file:
            json.dump(self.url_mapping, file)

    def shorten_url(self, long_url):
        if long_url in self.url_mapping.values():
            for short, long in self.url_mapping.items():
                if long == long_url:
                    return short

        short_url = f"http://short.url/{len(self.url_mapping) + 1}"
        self.url_mapping[short_url] = long_url
        self.save_data()
        return short_url

    def get_long_url(self, short_url):
        return self.url_mapping.get(short_url, "URL not found")


if __name__ == "__main__":
    url_shortener = URLShortener()

    while True:
        choice = input(
            "1. Shorten URL\n2. Get Long URL\n3. Exit\nChoose an option: ")
        if choice == '1':
            long_url = input("Enter the long URL: ")
            short_url = url_shortener.shorten_url(long_url)
            print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the short URL: ")
            long_url = url_shortener.get_long_url(short_url)
            print(f"Long URL: {long_url}")
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")
