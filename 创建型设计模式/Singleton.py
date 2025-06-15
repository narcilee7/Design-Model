# 单例模式

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.created = True
        return cls._instance

# 使用
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
