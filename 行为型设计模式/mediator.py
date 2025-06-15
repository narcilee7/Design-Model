# 中介者模式

# 抽象中介者
class Mediator:
    def notify(self, sender: object, event: str): pass

# 抽象同事类
class ColleagueA:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def do_sth(self, notify_mediator=True):
        print("同事A做了一些事")
        if notify_mediator:
            self.mediator.notify(self, "A")

class ColleagueB:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def do_sth(self, notify_mediator=True):
        print("同事B做了一些事")
        if notify_mediator:
            self.mediator.notify(self, "B")

# 具体中介者
class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleague_a = None
        self.colleague_b = None

    def set_colleague_a(self, colleague_a: ColleagueA):
        self.colleague_a = colleague_a

    def set_colleague_b(self, colleague_b: ColleagueB):
        self.colleague_b = colleague_b

    def notify(self, sender: object, event: str):
        if event == 'A':
            print("中介者通知同事B")
            # 调用时不通知中介者，避免递归
            self.colleague_b.do_sth(notify_mediator=False)
        elif event == 'B':
            print("中介者通知同事A")
            self.colleague_a.do_sth(notify_mediator=False)

# 使用
mediator = ConcreteMediator()
colleague_a = ColleagueA(mediator)
colleague_b = ColleagueB(mediator)

mediator.set_colleague_a(colleague_a)
mediator.set_colleague_b(colleague_b)

colleague_a.do_sth()
colleague_b.do_sth()
