class Animal(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def talk(self):
        raise NotImplementedError("Talk method not implemented")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)

    def talk(self):
        print("Meow")
        
    def show_affection(self):
        print("Purrrrrrrr")

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

    def __str__(self):
        return("I'm a dog. Woof Woof. My name is " + self.name)

    def talk(self):
        print("Bark")

if __name__ == "__main__":
    gwen = Cat("Quenevier")
    print(gwen)
    gwen.talk()
    gwen.show_affection()
    
    gruf = Dog("Gruffy")
    print(gruf)
    gruf.talk()
    
    animal_list = [Cat("Ruby"), Dog("Sammy"), 
                   Cat("Veda"), Dog("Old Yeller")]
    for animal in animal_list:
        print(animal)
        animal.talk()
    