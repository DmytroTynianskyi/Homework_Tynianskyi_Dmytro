# Завдання 2

# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.

class GraphicObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing object at ({self.x}, {self.y})")


class Rectangle(GraphicObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing rectangle at ({self.x}, {self.y}), size {
              self.width}x{self.height}")


class ClickableObject:
    def on_click(self):
        print("Object clicked!")


class Button(Rectangle, ClickableObject):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text

    def draw(self):
        print(f"Drawing button '{self.text}' at ({self.x}, {
              self.y}), size {self.width}x{self.height}")

    def on_click(self):
        print(f"Button '{self.text}' clicked!")


rect = Rectangle(10, 20, 100, 50)
rect.draw()

button = Button(30, 40, 120, 60, "OK")  
button.draw()
button.on_click()


