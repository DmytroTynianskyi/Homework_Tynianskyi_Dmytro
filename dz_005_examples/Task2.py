# Завдання 2
# Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact, sent_message.
# Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job. Додати методи get_message.
# Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.

class Contact:
    def __init__(self,surname:str,name:str,age:int,mob_phone:int,email:str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return self.surname,self.name,self.age,self.mob_phone,self.email

    def sent_message(self,message:str):
        self.message = message


class UpdateContact(Contact):
    def __init__(self, surname: str, name: str, age: int, mob_phone: int, email: str, job:str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email
        self.job = job

    def get_contact(self):
        return self.surname, self.name, self.age, self.mob_phone, self.email,self.job
    
    def get_message(self):
        try:
            return self.message
        except:
            print("Немає повідомлень")

mayor = UpdateContact("Mayor", "Leonov", 42, 123423453412, "Mayor@gmail.com","Programer")

print(mayor.get_contact())
mayor.sent_message("Hello world")
print(mayor.get_message())
print(mayor.__dict__)
# print(mayor.__base__)
# print(mayor.__bases__)



