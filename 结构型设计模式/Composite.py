# 组合模式

class Component:
  def operation(self): pass

class Leaf(Component):
  def __init__(self, name):
    self.name = name

  def operation(self):
    print(f"Leaf {self.name} operation")

class Composite(Component):
  def __init__(self):
    self.children = []

  def add(self, component: Component):
    self.children.append(component)

  def remove(self, component: Component):
    self.children.remove(component)

  def operation(self):
    for child in self.children:
      child.operation()

# run

root = Composite()

root.add(Leaf("Leaf A"))
root.add(Leaf("Leaf B"))

comp = Composite()
comp.add(Leaf("Leaf XA"))
comp.add(Leaf("Leaf XB"))

root.add(comp)

root.operation()