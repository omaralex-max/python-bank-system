class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."
    def drink(self):
        return f"{self.name} is drinking."

class Cat(Animal):
    def __init__(self, name, age, breed, color):
        # Initialize the base class (Animal)
        super().__init__(name, age, species="Cat")
        self.breed = breed
        self.color = color

    def eat(self):
        return f"{self.name} the {self.breed} cat is eating."

    def meow(self):
        return f"{self.name} is meowing."

if __name__ == "__main__":
    Ganimal = Animal("popsy", 5, "dog")
    print(Ganimal.eat())  
    print(Ganimal.sleep()) 

    kitty = Cat("mr.doodels", 3, "Siamese", "caramel")
    print(kitty.eat())  
    print(kitty.meow())  
    print(kitty.sleep()) 
