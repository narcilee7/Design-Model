# 原型模式
import copy

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def clone(self):
    return copy.deepcopy(self)

p1 = Person("Alice", 20)
p2 = p1.clone()
print(p1.name, p2.name)
print(p1 is p2)  # False
