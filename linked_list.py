from node import Node

class LinkedList:
    '''Made singly linked list'''
    def __init__(self):
        '''Create an empty linked list with head, tail, and a size counter.'''
        self._head = None
        self._tail = None
        self._len = 0 


    def add_first(self,item):
        '''Add an item to the beginning of the linked list.'''
        self._head = Node(item,self._head)
        if self._tail is None: self._tail = self._head
        self._len +=1
       
        
    def add_last(self,item):
        '''Add an item to the end of the linked list. '''
        if self._head is None:
            self.add_first(item) 
        else:
            self._tail.next= Node(item)
            self._tail = self._tail.next
            self._len +=1
        
    def remove_first(self):
        '''Remove and return the first item Return None if empty.'''
        if self._head is None:
            return None
        data = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._len -= 1
        return data
        
    def get_first(self):
        '''Return the first item without removing it. Return None if empty.'''
        if self._head is None:
            return None
        return self._head.data
        
    def is_empty(self):
        '''Return True when the linked list is empty.'''
        return self._len==0
            

    def size(self):
        '''Return the number of items in the linked list.'''
        return self._len
        
