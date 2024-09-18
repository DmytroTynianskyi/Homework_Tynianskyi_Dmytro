# Завдання 5
# Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact та їх екземплярах.
# Видаліть атрибут job,і знову надрукуйте стан класів та їх екземплярів. Порівняйте їх. Зробіть відповідні висновки.

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
            
# contact = Contact('John Doe', '123456789', 'Engineer')
# update_contact = UpdateContact('Jane Smith', '987654321', 'Doctor', 'jane.smith@email.com')
update_contact = UpdateContact("Mayor", "Leonov", 42, 123423453412, "Mayor@gmail.com", "Programer")
contact = Contact("Jeison", "Stethem", 52, 15356345112, "Jeison@gmail.com")
print("Before deleting 'job':")
print(contact)
print(update_contact)

try:
    delattr(contact, 'job')
except :
    pass
    
delattr(update_contact, 'job')

print("\nAfter deleting 'job':")

try:
    print(contact)
except AttributeError as e:
    print(f"Error in contact: {e}")

try:
    print(update_contact)
except AttributeError as e:
    print(f"Error in update_contact: {e}")


