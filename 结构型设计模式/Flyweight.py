# 享元模式

class Flyweight:
  def __init__(self, shared_state):
    self.shared_state = shared_state

  def operation(self, unique_state):
    print(f"共享状态: {self.shared_state}, 独享状态: {unique_state}")

class FlyweightFactory:
  def __init__(self): self._cache = {}

  def get_flyweight(self, shared_state):
    key = str(shared_state)
    if key not in self._cache:
        self._cache[key] = Flyweight(shared_state)
    return self._cache[key]

# run

factory = FlyweightFactory()
flyweight = factory.get_flyweight("共享状态")
flyweight.operation("独享状态")

flyweight2 = factory.get_flyweight("共享状态")
flyweight2.operation("独享状态2")

print(flyweight is flyweight2)