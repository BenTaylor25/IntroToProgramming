'''
my_dog_name = "Benji"
my_dog_age = 5
my_dog_breed = "Lab"

your_dog_name = "Bailey"
your_dog_age = 3
your_dog_breed = "Pug"

their_dog_name = "Bella"
their_dog_age = 6
their_dog_breed = "Poodle"
'''

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def get_info(self):
        print(self.name)
        print(self.age)
        print(self.breed)
        print()

    def speak(self):
        print(self.name + ": 'woof!'")
        
my_dog = Dog("Benji", 5, "Lab")
your_dog = Dog("Bailey", 3, "Pug")

my_dog.speak()
your_dog.speak()
