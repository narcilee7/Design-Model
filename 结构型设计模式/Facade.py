# 外观模式

class SubsysA:
  def operation_a(self):
    return "SubsysA operation"

class SubsysB:
  def operation_b(self):
    return "SubsysB operation"

class Facade:
  def __init__(self):
    self.subsys_a = SubsysA()
    self.subsys_b = SubsysB()

  def operation(self):
    result = "Facade initializes subsystems:\n"
    result += self.subsys_a.operation_a() + "\n"
    result += self.subsys_b.operation_b() + "\n"
    return result

# run
facade = Facade()
print(facade.operation())