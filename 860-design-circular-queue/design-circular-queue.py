class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.que = [0] * k  
        self.max_len = k 
        

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.que[self.rear] = value
            self.rear = (self.rear + 1) % self.max_len
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.que[self.front] = 0
            self.front = (self.front +1) % self.max_len
            return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.que[self.front]     

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.que[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.que[self.front] == 0
        

    def isFull(self) -> bool:
        return self.front == self.rear and self.que[self.front] != 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()