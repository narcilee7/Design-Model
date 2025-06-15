# 模板方法模式

from abc import ABC, abstractmethod

# 抽象类
class AbstractClass(ABC):
  def template_method(self):
    self.step_1()
    self.step_2()
    self.step_3()
    self.hook()

  def step_1(self):
    print("AbstractClass: 步骤一（通用实现）")

  @abstractmethod
  def step_2(self):
    pass

  def step_3(self):
    print("AbstractClass: 步骤三（通用实现）")

  # 钩子方法
  def hook(self):
    pass

# 具体类
class ConcreteClassA(AbstractClass):
  def step_2(self):
    print("ConcreteClassA: 实现步骤二")

# 具体类
class ConcreteClassB(AbstractClass):
  def step_2(self):
    print("ConcreteClassB: 实现步骤二")

  def hook(self):
    print("ConcreteClassB: 重写钩子方法")

# run
a = ConcreteClassA()
a.template_method()

b = ConcreteClassB()
b.template_method()