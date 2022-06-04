class PolyA:
    def __init__(self, msg="i am PolyA!!"):
        self._msg = msg

    def init(self):
        self.work()

    def work(self):
        print("PolyA is working")
        print("PolyA:work:msg=" + self._msg)


class PolyB(PolyA):
    def __init__(self):
        super().__init__("I am PolyB!!")

    def work(self):
        print("PolyB is working")
        print("PolyB:work:msg=" + self._msg)


a = PolyA()
a.init()
print()
b = PolyB()
b.init()
