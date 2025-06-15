# 桥接模式

# 分离抽象部分与其实现部分，使它们都可以独立地变化。

# 实现部分
class DrawingAPI:
  def draw_circle(self, x, y, radius):
    pass

class DrawingAPI1(DrawingAPI):
  def draw_circle(self, x, y, radius):
    print(f"API1 Drawing Circle[ x={x}, y={y}, radius={radius}]")

class DrawingAPI2(DrawingAPI):
  def draw_circle(self, x, y, radius):
    print(f"API2 Drawing Circle[ x={x}, y={y}, radius={radius}]")

# 抽象部分
class Shape:
  def draw(self): pass

class CircleShape(Shape):
  def __init__(self, x, y, radius, drawing_api):
    self.x = x
    self.y = y
    self.radius = radius
    self.drawing_api = drawing_api

  def draw(self):
    self.drawing_api.draw_circle(self.x, self.y, self.radius)

# 使用
circle1 = CircleShape(1, 2, 3, DrawingAPI1())
circle2 = CircleShape(4, 5, 6, DrawingAPI2())

circle1.draw()
circle2.draw()