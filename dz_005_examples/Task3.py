# Завдання 3
# Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr().
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.
import inspect 


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
print(hasattr(mayor,"surname"))
print(delattr(mayor, "surname"))
print(setattr(mayor, "surname","General"))
print(getattr(mayor, "surname"))