# 代理模式

class RealProject:
  def request(self):
    print("真实请求")

class Proxy:
  def __init__(self, real_project: RealProject):
    self.real_project = real_project

  def request(self):
    print("代理请求前置")
    self.real_project.request()
    print("代理请求后置")

# run
real_project = RealProject()
proxy = Proxy(real_project)
proxy.request()
