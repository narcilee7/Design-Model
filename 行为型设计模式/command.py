# 命令模式

class Command:
  def execute(self): pass

class Receiver:
  def action(self):
    print("执行操作")

class ConcreteCommand(Command):
  def __init__(self, receiver: Receiver):
    self.receiver = receiver

  def execute(self):
    self.receiver.action()

class Invoker:
  def __init__(self):
    self.command = None
  def set_command(self, command):
    self.command = command
  def run(self):
    self.command.execute()

# 使用
receiver = Receiver()
cmd = ConcreteCommand(receiver)
invoker = Invoker()
invoker.set_command(cmd)
invoker.run()