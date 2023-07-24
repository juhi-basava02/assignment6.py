

class Dog:
    def _init_(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("The dog's name is {self.name} and it is {self.age} years old.")

    def get_info(self):
        print("The dog's coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def _init_(self, name, age, coat_color, energy_level):
        super()._init_(name, age, coat_color)
        self.energy_level = energy_level
    def play(self):
        print("The Jack Russell Terrier, {self.name}, is playing.")

    def bark(self):
        print("The Jack Russell Terrier, {self.name}, is barking.")


class Bulldog(Dog):
    def _init_(self, name, age, coat_color, weight):
        super()._init_(name, age, coat_color)
        self.weight = weight

    def eat(self):
        print("The Bulldog, {self.name}, is eating.")

    def sleep(self):
        print("The Bulldog, {self.name}, is sleeping.")
if __name__ == "_main_":
    dog = Dog("Spot", 5, "brown")
    dog.description()
    dog.get_info()

    jack_russell_terrier = JackRussellTerrier("Jack", 3, "white", 10)
    jack_russell_terrier.description()
    jack_russell_terrier.get_info()
    jack_russell_terrier.play()
    jack_russell_terrier.bark()

    bulldog = Bulldog("Rocky", 7, "red", 50)
    bulldog.description()
    bulldog.get_info()
    bulldog.eat()
    bulldog.sleep()