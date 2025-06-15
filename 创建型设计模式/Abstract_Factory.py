# 抽象工厂模式

# 抽象产品
class Button:
  def render(self):
    pass

# 具体产品
class MacButton(Button):
  def render(self):
    print("MacButton render")

class WindowsButton(Button):
  def render(self):
    print("WindowsButton render")

# 抽象工厂
class GUIFactory:
  def create_button(self):
    pass

# 具体工厂
class MacFactory(GUIFactory):
  def create_button(self):
    return MacButton()

class WindowsFactory(GUIFactory):
  def create_button(self):
    return WindowsButton()
  
