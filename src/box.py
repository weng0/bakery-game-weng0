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

# stack = Box_Stack()
# for b in range(3):
#     stack.boxes.append(Box())

# for b in stack.boxes:
#     print(b)

# <__main__.Box object at 0x000001C778ADFD60>
# <__main__.Box object at 0x000001C778ADFD30>
# <__main__.Box object at 0x000001C778ADF8B0>