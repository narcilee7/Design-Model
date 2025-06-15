# 解释器模式
from abc import ABC, abstractmethod

# True AND False OR True 目标解析这样的表达式
target = "True AND False OR True"

# 抽象表达式
class Expression(ABC):
  @abstractmethod
  def interpret(self) -> bool: pass

# 终结符表达式
class BooleanValue(Expression):
  def __init__(self, value: bool):
      self.value = value

  def interpret(self) -> bool:
      return self.value

# 非终结符表达式
class AndExpression(Exception):
  def __init__(self, left: Expression, right: Expression):
    self.left = left
    self.right = right

  def interpret(self) -> bool:
    return self.left.interpret() and self.right.interpret()

class OrExpression(Exception):
  def __init__(self, left: Expression, right: Expression):
    self.left = left
    self.right = right

  def interpret(self) -> bool:
    return self.left.interpret() or self.right.interpret()

if __name__ == "__main__":
  expression = BooleanValue(True)
  print(expression.interpret())

  expression = AndExpression(BooleanValue(True), BooleanValue(False))
  print(expression.interpret())

  expression = OrExpression(BooleanValue(True), BooleanValue(False))
  print(expression.interpret())