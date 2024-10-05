# Завдання 1

# Перепишіть домашнє завдання попереднього уроку(сервіс для скорочення посилань) таким чином,
# щоб у нього була основна частина, яка відповідала би за логіку роботи та надавала узагальнений інтерфейс,
# і модуль представлення, який відповідав би за взаємодію з користувачем. При заміні останнього на інший,
# який взаємодіє з користувачем в інший спосіб, програма має продовжувати коректно працювати.

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        if long_url in self.url_mapping.values():
            for short, long in self.url_mapping.items():
                if long == long_url:
                    return short

        short_url = f"http://short.url/{len(self.url_mapping) + 1}"
        self.url_mapping[short_url] = long_url
        return short_url

    def get_long_url(self, short_url):
        return self.url_mapping.get(short_url, "URL not found")
