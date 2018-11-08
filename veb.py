def high(x, size):
    return x//(size ** 0.5)
def low(x, size):
    return x%(size ** 0.5)

class vEB:
    def __init__(self, size):
        self.size = size
        self.maximum = None
        self.minimum = None
        self.summary = []
        self.cluster = []
    def tree_member(self, x):
        if x == self.minimum or x == self.maximum:
            return True
        elif self.size==2:
            return False
        else: return self.cluster[high(x,self.size)].tree_member(low(x,self.size))