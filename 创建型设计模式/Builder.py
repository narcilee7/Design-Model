# 建造者模式

# 产品

class Product:
  def __init__(self):
    self.parts = []

  def add(self, part):
    self.parts.append(part)

  def show(self):
    print("Product parts:", ", ".join(self.parts))

# 建造者
class Builder:
    def __init__(self):
        self.product = Product()

    def add_part_a(self):
        self.product.add("PartA")
        return self

    def add_part_b(self):
        self.product.add("PartB")
        return self

    def build(self):
        return self.product
