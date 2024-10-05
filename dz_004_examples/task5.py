# Завдання 5

# Створіть програму спортивного комплексу, у якій передбачене
# меню: 1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань, 4 - вартість тренування.
# Дані зберігати у словниках. Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню.
# Якщо ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.

class TrainerNotFound(Exception):
    def __init__(self, message="Trainer not found"):
        self.message = message
        super().__init__(self.message)


sports = {
    1: "Football",
    2: "Basketball",
    3: "Tennis"
}

trainers = {
    "Smith": ["Football", "Basketball"],
    "Johnson": ["Tennis"]
}

schedule = {
    "Football": "Mon, Wed, Fri - 18:00",
    "Basketball": "Tue, Thu - 19:00",
    "Tennis": "Sat - 10:00"
}

prices = {
    "Football": 100,
    "Basketball": 120,
    "Tennis": 80
}


def find_trainer(name):
    if name not in trainers:
        raise TrainerNotFound(f"Trainer '{name}' not found in the system.")
    return trainers[name]


def menu():
    while True:
        print("\nMenu:")
        print("1 - List of sports")
        print("2 - Trainer team")
        print("3 - Training schedule")
        print("4 - Training cost")
        print("5 - Search trainer by last name")
        print("0 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nSports available:")
            for sport in sports.values():
                print(sport)
        elif choice == '2':
            print("\nTrainer team:")
            for trainer, sports_list in trainers.items():
                print(f"{trainer}: {', '.join(sports_list)}")
        elif choice == '3':
            print("\nTraining schedule:")
            for sport, time in schedule.items():
                print(f"{sport}: {time}")
        elif choice == '4':
            print("\nTraining cost:")
            for sport, price in prices.items():
                print(f"{sport}: {price} UAH")
        elif choice == '5':
            try:
                name = input("Enter trainer's last name: ")
                found_sports = find_trainer(name)
                print(f"Trainer {name} is responsible for: {
                      ', '.join(found_sports)}")
            except TrainerNotFound as tnfe:
                print(f"Error: {tnfe}")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
