class MinStack:

    def __init__(self):
        self.stack = []
        self.mint = []

    def push(self, val: int) -> None:
        s = self.stack
        m = self.mint
        s.append(val)
        if len(m) == 0 or m[-1] > val:
            m.append(val)
        else:
            m.append(m[-1])
        
    
    def pop(self) -> None:
        s = self.stack
        m = self.mint
        del m[-1]
        del s[-1]


    def top(self) -> int:
        s = self.stack
        return s[-1]

    def getMin(self) -> int:
        m = self.mint
        return m[-1]

        
