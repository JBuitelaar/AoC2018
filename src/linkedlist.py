"""doubly linked list"""

class Node:
    def __init__(self,value,prev,next):
        self.value=value
        self.prev=prev
        self.next=next

    def move_left(self,steps:int):
        assert steps>0
        if steps == 1:
            return self.prev
        else:
            return self.prev.move_left(steps-1)

    def move_right(self,steps:int):
        assert steps>0
        if steps==1:
            return self.next
        else:
            return self.next.move_right(steps-1)

    def insert_before(self,value):
        new=Node(value,self.prev,self)
        self.prev.next=new
        self.prev=new
        return new

    def remove(self):
        """returns the next element"""
        self.prev.next=self.next
        self.next.prev=self.prev
        return self.next

    def print(self):
        values=[self.value]
        item=self.next
        while item!=self:             
            values.append(item.value)
            item=item.next
        print("->".join(str(x) for x in values))

    def __str__(self):
        return "->".join(str(x) for x in [self.prev.value,self.value,self.next.value])

def circle1(value=0):
    """Circle with 1 element"""
    res=Node(value,None,None)
    res.prev=res
    res.next=res
    return res