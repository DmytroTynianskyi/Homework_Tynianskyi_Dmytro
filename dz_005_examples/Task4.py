# Завдання 4
# Використовуючи код з завдання 2, створити 2 екземпляри обох класів.
# Використати функції isinstance() – для перевірки екземплярів класу(за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка.

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
jeison = Contact("Jeison", "Stethem", 52, 15356345112, "Jeison@gmail.com")

# print(mayor.get_contact())
# mayor.sent_message("Hello world")
# print(mayor.get_message())
# print(mayor.__dict__)
# print(mayor.__base__)
# print(mayor.__bases__)
print(issubclass(UpdateContact,Contact))
print(issubclass(Contact, UpdateContact))
print(isinstance(jeison, Contact))
print(isinstance(mayor, UpdateContact))