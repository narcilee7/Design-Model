# 访问者模式

from abc import ABC, abstractmethod

# 访问者接口
class Visitor(ABC):
  @abstractmethod
  def visit_el_a(self, el): pass

  @abstractmethod
  def visit_el_b(self, el): pass

# 具体访问者
class ConcreteVisitorA(Visitor):
  def visit_el_a(self, el):
    print(f"ConcreteVisitorA: 访问元素A, 元素内容: {el.value}")

  def visit_el_b(self, el):
    print(f"ConcreteVisitorA: 访问元素B, 元素内容: {el.value}")

# 抽象元素
class Element(ABC):
  @abstractmethod
  def accept(self, visitor: Visitor): pass

# 具体元素A
class ConcreteElementA(Element):
  def __init__(self, value: int):
    self.value = value
    
  def accept(self, visitor: Visitor):
    visitor.visit_el_a(self)

# 具体元素B
class ConcreteElementB(Element):
  def __init__(self, value: int):
    self.value = value
    
  def accept(self, visitor: Visitor):
    visitor.visit_el_b(self)

# 对象结构
class ObjectStructure:
  def __init__(self):
    self.elements = []

  def add_element(self, element: Element):
    self.elements.append(element)

  def remove_element(self, element: Element):
    self.elements.remove(element)

  def accept(self, visitor: Visitor):
    for element in self.elements:
      element.accept(visitor)

obj_struct = ObjectStructure()
obj_struct.add_element(ConcreteElementA(10))
obj_struct.add_element(ConcreteElementB(20))

visitor = ConcreteVisitorA()
obj_struct.accept(visitor)