# Завдання 3

# Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.

import pickle
import json

products = [
    {"id": 1, "name": "Ноутбук", "price": 1500, "quantity": 10},
    {"id": 2, "name": "Смартфон", "price": 800, "quantity": 25},
    {"id": 3, "name": "Планшет", "price": 600, "quantity": 15},
    {"id": 4, "name": "Фітнес-трекер", "price": 200, "quantity": 50},
    {"id": 5, "name": "Ігрова консоль", "price": 500, "quantity": 5},
]

serialized_products = pickle.dumps(products)

products_json = {
    "products": list(serialized_products)
}

with open("products.json", "w") as json_file:
    json.dump(products_json, json_file)
