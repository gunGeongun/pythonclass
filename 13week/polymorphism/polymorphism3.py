class PolyA:
    def __init__(self):
        self.init()

    def init(self):
        self._msg = "I am PolyA!!"
        print('PolyA:init:msg=' + self._msg)

    def doing(self):
        self.work()
        print("PolyA:doing:msg=" + self._msg)

    def work(self):
        print("PolyA is working")
        print("PolyA:work:msg=" + self._msg)


class PolyB(PolyA):
    def __init__(self):
        self._msg = "I am PolyB!!"
        super().__init__()

    def init(self):
        print('PolyB:init:msg =' + self._msg)

    def work(self):
        print("PolyB is working")
        print("PolyB:work:msg=" + self._msg)


a = PolyA()
a.doing()
print()
b = PolyB()
b.doing()
