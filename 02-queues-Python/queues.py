"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        l = self.storage[::-1]
        l.append(new_element)
        self.storage = l[::-1]

    def peek(self):
        return self.storage[-1] 

    def dequeue(self):
        dequeued = self.storage.pop()
        return dequeued