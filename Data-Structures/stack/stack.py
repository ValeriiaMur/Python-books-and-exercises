"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import singly_linked_list 
# class Stack:

#     def __init__(self):
#         self.size = 0
#         self.items = []
#         # self.storage = ?

#     def __len__(self):
#         return len(self.items)

#     def push(self, value):
#         self.items.append(value)

#     def pop(self):
#         if(len(self.items) != 0):
#             val = self.items.pop()
#             return val
            

class Stack:
    def __init__(self):
        self.head = None
        # self.storage = ?

    def __len__(self):
        # return len(self.items)
        pass

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if(len(self.items) != 0):
            val = self.items.pop()
            return val
