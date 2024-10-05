# Завдання 1

# Створіть клас Editor, який містить методи view_document та edit_document.
# Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для безкоштовної версії.
# Створіть підклас ProEditor, у якому цей метод буде перевизначено.
# Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor.
# Викликайте методи перегляду та редагування документів.

class Editor:
    def view_document(self):
        """Метод для перегляду документа"""
        print("Viewing document...")

    def edit_document(self):
        """Метод для редагування документа у безкоштовній версії"""
        print("Editing is not available in the free version.")


class ProEditor(Editor):
    def edit_document(self):
        """Перевизначений метод для редагування документа у Pro версії"""
        print("Editing document...")



LICENSE_KEY = "PRO123"
user_key = input("Enter your license key: ")

if user_key == LICENSE_KEY:
        editor = ProEditor()
        print("Pro version activated.")
else:
        editor = Editor()
        print("Free version activated.")

editor.view_document()
editor.edit_document()


