# 观察者模式
from abc import ABC, abstractmethod

# 抽象主题(被观察者)
class Subject(ABC):
  def __init__(self):
    # 观察者列表
    self._observers = []
  
  def attach(self, observer: any):
    self._observers.append(observer)

  def detach(self, observer: any):
    self._observers.remove(observer)

  def notify(self, state: any):
    for observer in self._observers:
      observer.update(state)

# 抽象观察者
class Observer(ABC):
  @abstractmethod
  def update(self, state: any): pass

# 具体主题
class ConcreteSubject(Subject):
  def __init__(self):
    super().__init__()
    self._state = None

  @property
  def state(self):
    return self._state

  @state.setter
  def state(self, value: any):
    self._state = value
    self.notify(value) # 状态改变，通知观察者

# 具体观察者
class ConcreteObserver(Observer):
  def __init__(self, name):
      self.name = name
  def update(self, state: any):
      print(f"{self.name} 收到通知，主题状态变为: {state}")

# 使用
subject = ConcreteSubject()
observer1 = ConcreteObserver("观察者1")
observer2 = ConcreteObserver("观察者2")

subject.attach(observer1)
subject.attach(observer2)

subject.state = "状态1"
subject.state = "状态2"
subject.state = "状态3"

subject.detach(observer1)
subject.state = "状态4"