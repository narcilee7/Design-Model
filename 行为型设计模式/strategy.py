# 策略模式
from abc import ABC, abstractmethod

# 抽象策略类
class Strategy(ABC):
  @abstractmethod
  def do_algorithm(self): pass

# 具体策略A
class ConcreteStrategyA(Strategy):
  def do_algorithm(self, data: list):
    print("执行策略A")
    return sorted(data)

# 具体策略B
class ConcreteStrategyB(Strategy):
  def do_algorithm(self, data: list):
    print("执行策略B")
    return sorted(data, reverse=True)

# 上下文
class Context:
  def __init__(self, strategy: Strategy):
    self.strategy = strategy

  def set_strategy(self, strategy: Strategy):
    self.strategy = strategy

  def do_something(self, data: list):
    return self.strategy.do_algorithm(data)

# 使用
context = Context(None)
context.set_strategy(ConcreteStrategyA())
print(context.do_something([3, 1, 2]))

context.set_strategy(ConcreteStrategyB())
print(context.do_something([3, 1, 2]))

