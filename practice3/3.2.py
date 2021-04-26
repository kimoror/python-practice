class C32:
    def __init__(self):
        self.state: C32.State = C32.A(self)

    def hoard(self) -> int:
        return self.state.hoard()

    def skid(self) -> int:
        return self.state.skid()

    def walk(self) -> int:
        return self.state.walk()


class State:
    def __init__(self, parent):
        self.parent: C32 = parent

    def hoard(self) -> int:
        raise RuntimeError

    def skid(self) -> int:
        raise RuntimeError

    def walk(self) -> int:
        raise RuntimeError


class A(State):

    def hoard(self):
        self.parent.state = C32.B(self.parent)
        return 0


class B(State):

    def hoard(self):
        self.parent.state = C32.C(self.parent)
        return 2


class C(State):
    def skid(self):
        self.parent.state = C32.D(self.parent)
        return 2


class D(State):
    def walk(self):
        self.parent.state = C32.F(self.parent)
        return 6

    def apply(self):
        self.parent.state = C32.H(self.parent)
        return 5

    def hoard(self):
        self.parent.state = C32.E(self.parent)
        return 3

    def skid(self):
        self.parent.state = C32.G(self.parent)
        return 4

class E(State):
    def hoard(self):
        self.parent.state = C32.F(self.parent)
        return 7


class F(State):
    def skid(self):
        self.parent.state = C32.G(self.parent)
        return 8


class G(State):
    def walk(self):
        self.parent.state = C32.H(self.parent)
        return 9

    def apply(self):
        self.parent.state = C32.A(self.parent)
        return 10


class H(State):
    def skid(self):
        self.parent.state = C32.H(self.parent)
        return 11
