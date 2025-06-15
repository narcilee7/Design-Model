# 工厂方法模式

# 动物类
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")
# 动物工厂  
class AnimalFactory:
    def create_animal(self):
        pass
# 🐶🐶工厂
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()
# 🐱🐱工厂
class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# 使用
dog_factory = DogFactory()
dog = dog_factory.create_animal()
dog.speak()

cat_factory = CatFactory()
cat = cat_factory.create_animal()
cat.speak()