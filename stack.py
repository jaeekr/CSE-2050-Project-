from linked_list import LinkedList
class Stack:
  def __init__(self):
    self._list = LinkedList()
    
  def push(self, item):
    self._list.add_first(item)
    
  def pop(self):
    self._list.remove_first()
    
  def peek(self):
    return self._list.head.data
    
  def is_empty(self):
    if self.is_empty():
      return None
    return self._list.head.data
    
  def size(self):
    return self._list.size
