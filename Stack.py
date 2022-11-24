# Jayden Yap p2112790 DAAA/2B/04 DSAA CA1 stack.py
#use linked list for our stack as it is a appropriate data structure for accessing elements only at the edge of structure
class _Node:
    '''
    Creates a Node with two fields:
    1. element (accesed using .element)
    2. link (accesed using .link)
    '''
    __slots__ = 'element', 'link'

    def __init__(self, element, link):
        '''
        Initialses element and link with element and link respectively.
        '''
        self.element = element
        self.link = link


class StackLL:
    '''
    Consists of member funtions to perform different
    operations on the linked list.
    '''

    def __init__(self):
        '''
        Initialses head, tail and size with None, None and 0 respectively.
        '''
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        '''
        Returns length of stack.
        '''
        return self.size

    def isempty(self):
        '''
        Returns True if stack is empty, otherwise False.
        '''
        return self.size == 0

    def push(self, e):
        '''
        Pushes the passed element at the beginning of the linked list.
        That means, on the top of our stack.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            newest.link = self.head
            self.head = newest
        self.size += 1

    def pop(self):
        '''
        Removes element from the beginning of the linked list.
        That means, pops element that is on the top.
        Returns the removed element.
        '''
        if self.isempty():
            print("Stack is Empty. Cannot perform Pop operation.")
            return

        e = self.head.element
        self.head = self.head.link
        self.size = self.size - 1

        if self.isempty():
            self.tail = None

        return e
    
    def top(self):
        '''
        Peeks at the element on the top of the stack.
        '''
        if self.isempty():
            print("Stack is Empty. Cannot perform Pop operation.")
            return

        e = self.head.element
        return e

    def display(self):
        '''
        Utility function to display the Stack.
        '''
        if self.isempty() == 0:
            p = self.head
            while p:
                print(p.element)
                p = p.link
        else:
            print("Empty")

#specific class with menu-specific function
class menuStackLL(StackLL):
    def __init__(self):
        super().__init__()

    #iterate through stack like a list 
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.link
    
    def resetToMain(self):
        #empty the stack
        size=self.size
        while self.size!=0:
            self.pop()
        #add main menu item
        self.push('MAIN')