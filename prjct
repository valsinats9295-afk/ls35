class Human():
    def __init__(self, age, male, hunger=0, energy=100, health=100, height=180, dollars=100, job=None, car=None, house=None):
        self.age = age
        self.male = male
        self.hunger = hunger
        self.energy = energy
        self.health = health
        self.height = height
        self.dollars = dollars
        self.job = job
        self.car = car
        self.house = house

    def sleep(self):
        self.energy = 100
        self.hunger += 15

    def eat(self):
        if self.energy <= 90:
            self.energy += 10
        self.hunger = 0

    def get_work(self, distance = 4):
        self.car.drive(distance)
        self.car.get_info()

    def work(self, hours_worked):
        if self.energy >= (hours_worked * 10):
            self.dollars += (hours_worked * 5)
            self.energy -= (hours_worked * 10)
        else:
            print("I'm too tired, I need to sleep!!!")

    def shopping(self, spent_money = 15):
        self.dollars -= spent_money

    def rentral_payment(self):
        self.dollars -= 50

    def get_info(self):
        print("Energy: ", self.energy, " Hunger: ", self.hunger, " Balance: ", self.dollars)

    def buy_car(self):
        if self.dollars >= 150:
            self.dollars -= 150
            self.car = Auto(6, 40, "Skoda")

    def clean_house(self):
        if self.house is None:
            print("No house to clean!")
            return

        if self.energy >= 20:
            self.energy -= 20
            self.house.mess = 0
        else:
            print("Too tired to clean!")


class Auto:
    def __init__(self, consumption = 10, fuel = 30, brand = "Bently"):
        self.consumption = consumption
        self.fuel = fuel
        self.brand = brand

    def drive(self, distance = 15):
        self.fuel -= self.consumption * (distance / 10)

    def get_info(self):
        print("Fuel: ", self.fuel)


class House:
    def __init__(self, facade_color="White", rooms=3, mess=50):
        self.facade_color = facade_color
        self.rooms = rooms
        self.mess = mess
