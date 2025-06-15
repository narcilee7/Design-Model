# 责任链模式

class Handler:
  def __init__(self, successor=None):
    self.successor = successor

  def handle(self, request):
    if self.successor:
      return self.successor.handle(request)
    print("No handler found")
    return None

class ConcreteHandlerA(Handler):
  def handle(self, request):
    if request < 10:
        return f"A处理了{request}"
    return super().handle(request)

class ConcreteHandlerB(Handler):
  def handle(self, request):
    if request < 20:
        return f"B处理了{request}"
    return super().handle(request)
    
# run
h = ConcreteHandlerA(ConcreteHandlerB())
print(h.handle(15))