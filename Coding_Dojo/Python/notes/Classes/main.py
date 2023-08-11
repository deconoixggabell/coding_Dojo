class Animal:
    def __init__(self, type, name, age) -> None:
        self.type = type
        self.name = name
        self.age = age

    def eat(self,):
        print(f"The {self.name} eats {self.type} food")

cat1 = Animal("cat", "babou", 5)
cat1.eat()
cat2 = Animal("cat", "lala", 10)
cat2.eat()

dog1 = Animal("dog", "poochie", 2)
dog1.eat()

# print(animal1.name)
# print(animal2.name)

