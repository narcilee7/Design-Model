# 状态模式

from abc import ABC, abstractmethod

# 抽象状态类
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# 具体状态A
class ConcreteStateA(State):
    def handle(self, context):
        print("当前状态：状态A，切换到状态B")
        context.state = ConcreteStateB()

# 具体状态B
class ConcreteStateB(State):
    def handle(self, context):
        print("当前状态：状态B，切换到状态A")
        context.state = ConcreteStateA()

# 上下文
class Context:
    def __init__(self, state: State):
        self.state = state

    def request(self):
        self.state.handle(self)

# 使用
context = Context(ConcreteStateA())
context.request()  # 当前状态：状态A，切换到状态B
context.request()  # 当前状态：状态B，切换到状态A
context.request()  # 当前状态：状态A，切换到状态B
