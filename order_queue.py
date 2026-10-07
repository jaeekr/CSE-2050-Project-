from linked_list import LinkedList
class OrderQueue:

    def __init__(self):
        '''initializes a queue as a Linked List'''
        self.queue = LinkedList()

    def enqueue(self, item):
        '''adds an item to the end of queue'''
        self.queue.add_last(item)

    def dequeue(self):
        '''checks if the queue is empty first, if not itremoves the first item in the queue while also returning it'''
        if self.queue.is_empty() == True:
            return None
        return self.queue.remove_first()

    def peek(self):
        '''checks if the queue is empt first, if not it returns the first item in queue'''
        if self.queue.is_empty() == True:
            return None
        return self.queue.get_first()

    def is_empty(self):
        '''returns if the queue is empty or not'''
        return self.queue.is_empty()

    def size(self):
        '''returns the size of the queue'''
        return self.queue.size()
    
