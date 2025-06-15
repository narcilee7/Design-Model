# 适配器模式

# 目标接口
class Target:
  def request(self):
    return '普通请求'
  

# 需要适配的类
class Adaptee:
  def specific_request(self):
    return '特殊请求'

# 适配器
class Adapter(Target):
  def __init__(self, adaptee: Adaptee):
    self.adaptee = adaptee

  def request(self):
    return f"适配器转化：{self.adaptee.specific_request()}"

# 使用
target = Target()
adaptee = Adaptee()
adapter = Adapter(adaptee)
print(target.request())
print(adapter.request())


