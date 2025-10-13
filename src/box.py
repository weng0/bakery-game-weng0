from bread import Bread

class Box:
    def __init__(self):
        self.bread_list : Bread = [None]*9 # index 0 - 8

    def isFull(self) -> bool:
        full = True
        for b in self.bread_list:
            if b == None:
                full = False
        return full

class Box_Stack:
    def __init__(self):
        self.boxes : Box = []