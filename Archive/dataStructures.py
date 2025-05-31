class Stack:
    def __init__(self, stack=None):
        self.stack = [] if stack is None else stack

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return None if self.is_empty() else self.stack.pop()
    
    def peek(self):
        return None if self.is_empty() else self.stack[-1]
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0

class Queue:
    def __init__(self, que=None):
        self.que = [] if que is None else que
    
    def enqueue(self, val):
        self.que.append(val)

    def dequeue(self):
        return None if self.is_empty() else self.que.pop(0)

    def head(self):
        return None if self.is_empty() else self.que[0]
    
    def is_empty(self) -> bool:
        return len(self.que) == 0
        
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def set_next(self, next):
        self.next = next

    def has_next(self) -> bool:
        return self.next is not None
    
def breath_first_search(root: Node, x) -> bool:
    queue: Queue = Queue([root])
    while not queue.is_empty():
        root = queue.dequeue()
        if root.val == x:
            return True
        elif root.has_next():
            for child in root.next:
                queue.enqueue(child)
    return False

def depth_first_search1(stack: Stack, x) -> bool:
    if stack.is_empty():
        return False
    for child in stack.peek().next:
        if child.val == x:
            return True
        elif child.has_next():
            depth_first_search1(stack.push(child))

def depth_first_search(root: Node, x) -> bool:
    stack: Stack = Stack([root])
    return depth_first_search1(stack, x)
        

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
root = node1
root.set_next([node2, node3, node4])
node2.set_next([node5, node6])
node4.set_next([node7])

if __name__ == '__main__':
    print(breath_first_search(root, 2))
    import numpy as np
    print(np.zeros((4, 1)))