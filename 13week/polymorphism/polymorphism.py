class PolyA:
    def __init__(self, msg="i am PolyA!!"):
        self.msg = msg

    def work(self):
        print("PolyA is working")
        print("PolyA:work:msg=" + self.msg)


class PolyB(PolyA):
    def __init__(self):
        super().__init__("I am PolyB!!")

    def work(self):
        print("PolyB is working")
        print("PolyB:work:msg=" + self.msg)


a = PolyA()
a.work()
b = PolyB()
b.work()
