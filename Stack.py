class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self): #boolean is it empty?
         return self.items == []

     def push(self, item): #add item to top of stack
         self.items.append(item)

     def pop(self): #remove item from top of stack
         return self.items.pop()

     def peek(self): #get first element of stack (at the top)
         return self.items[len(self.items)-1]

     def size(self): #length
         return len(self.items)