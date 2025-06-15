# 备忘录模式

class Memento:
  def __init__(self, state: any):
    self.state = state

  def get_state(self):
    return self.state

# 发起人，创建和恢复状态
class Originator:
  def __init__(self):
    self.state = None
    
  def set_state(self, state: any):
    self.state = state
    print(f"发起人状态改变为: {state}")

  def restore_state(self, memento: Memento):
    self.state = memento.get_state()
    print(f"发起人状态恢复为: {self.state}")

  def save_state(self, memento: Memento):
    print("保存当前状态")
    memento.state = self.state
    return memento

# 管理员，管理备忘录
class Caretaker:
  def __init__(self):
    self.mementos = []

  def add_memento(self, memento: Memento):
    self.mementos.append(memento)

  def get_memento(self, index: int):
    return self.mementos[index]

# 使用
originator = Originator()
caretaker = Caretaker()
memento = Memento("初始状态")

# 保存状态
originator.set_state("状态1")
originator.save_state(memento)

originator.set_state("状态2")
# originator.save_state(memento)

originator.set_state("状态3")
# originator.save_state(memento)

originator.set_state("状态4")
# originator.save_state(memento)

# 恢复状态
originator.restore_state(memento)
