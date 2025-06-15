# 装饰模式

class Component:
    def operation(self): pass

class ConcreteComponent(Component):
    def operation(self):
        return "基础功能"

class Decorator(Component):
    def __init__(self, component: Component):
        self.component = component

    def operation(self):
        return self.component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"{super().operation()} + 功能A"

# run
base = ConcreteComponent()
decorated = ConcreteDecoratorA(base)
print(decorated.operation())


