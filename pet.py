class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        print(f"Creating pet: {self.name}")

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness += 1
        print(f"{self.name} is eating...")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} is sleeping...")

    def play(self):
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1
        print(f"{self.name} is playing...")

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        return self.tricks

    def get_status(self):
        print(f"""{self.name}'s current status:
Hunger: {self.hunger}
Energy: {self.energy}
Happiness: {self.happiness}
Tricks: {Pet.show_tricks(self)}""")
