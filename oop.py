class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")

    def get_info(self):
        print(f"Brand: {self.brand}, Model: {self.model} with Storage: {self.storage}GB, Price: ${self.price}")
        

phone = Smartphone("Apple", "iPhone 13", 128, 999)
phone.get_info()
phone.call("07054785799")


class Gamingphone(Smartphone):
    def __init__(self, brand, model, storage, price, cooling_system):
        super().__init__(brand, model, storage, price)
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model} with {self.cooling_system} cooling system")

gaming_phone = Gamingphone("Asus", "ROG Phone 6", 521, 1299, "Advanced")        
gaming_phone.get_info()
gaming_phone.call("07054785799")
gaming_phone.play_game("Mobile Legends")


# The Polymorphism Example
class Vehicle:
    def start_engine(self):
        print("Starting the engine of the vehicle")

class Car(Vehicle):
    def start_engine(self):
        print("Starting the engine of the car with a roar!")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Starting the engine of the motorcycle with a vroom!")

class Truck(Vehicle):
    def start_engine(self):
        print("Starting the engine of the truck with a rumble!")


vehicles = [Car(), Motorcycle(), Truck()]
for vehicle in vehicles:
    vehicle.start_engine()