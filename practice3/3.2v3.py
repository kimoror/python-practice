class C32:
    def __init__(self):
        self.condition = 'A'

    def hoard(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'B':
            self.condition = 'C'
            return 1
        elif self.condition == 'D':
            self.condition = 'E'
            return 3
        elif self.condition == 'E':
            self.condition = 'F'
            return 7
        else:
            RuntimeError

    def skid(self):
        if self.condition == 'C':
            self.condition = 'D'
            return 2
        elif self.condition == 'D':
            self.condition = 'G'
            return 4
        elif self.condition == 'F':
            self.condition = 'G'
            return 8
        elif self.condition == 'H':
            self.condition = 'H'
            return 11
        else:
            RuntimeError

    def apply(self):
        if self.condition == 'D':
            self.condition = 'H'
            return 5
        if self.condition =='G':
            self.condition = 'A'
            return 10
        else:
            RuntimeError

    def walk(self):
        if self.condition == 'D':
            self.condition = 'F'
            return 6
        if self.condition == 'G':
            self.condition = 'H'
            return 9
        else:
            RuntimeError