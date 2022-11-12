class Stack:
     def __init__(self):
         self.__items = []

     def isEmpty(self): #boolean is it empty?
         return self.__items == []

     def push(self, item): #add item to top of stack
         self.__items.append(item)

     def pop(self): #remove item from top of stack
         return self.__items.pop()

     def peek(self): #get first element of stack (at the top)
         return self.__items[len(self.__items)-1]

     def size(self): #length
         return len(self.__items)

     def getList(self):
        return self.__items

#child class only for when the stack represents a menu
class menu_stack(Stack):
    def __init__(self):
        super().__init__()
    
    def resetToMain(self):
        self._Stack__items= ['MAIN']
