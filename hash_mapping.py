from entry import Entry

class HashMapping:
    def __init__(self, size=2):
        '''Create the bucket table and initialize the number
of stored key-value pairs. '''
        self.size = size #this is number of buckets 
        self._len = 0 #this is number of items
        self._L = [[] for i in range(self.size)]  #list containing all buckets 

    def __len__(self):
        '''Return the number of key-value pairs currently
stored'''
        return self._len
    
    def __contains__(self, key):
        '''Return True when key is stored in the mapping;
otherwise False.'''
        if self._find_entry(key) is None:
            return False
        else:
            return True

    def _find_entry(self,key):
        '''finding entry'''
        bucket_ind = hash(key) % self.size
        for entry in self._L[bucket_ind]:
            if key == entry.key: 
                return entry
        return None 

    def put(self,key,value):
        '''Add a new key-value pair or update the value for
an existing key. Use a hash to choose a bucket.'''
        if self.__contains__(key) is True: # already existed?
           entry = self._find_entry(key)
           entry.value = value 
           return
        new = Entry(key,value)
        bucket_index = hash(key) % self.size #create the new entry and place
        self._L[bucket_index].append(new)
        self._len += 1
        if self._len >= self.size : #rehash if needed 
            self.rehash()

    def get(self,key):
        '''Return the value associated with key. Raise
KeyError if the key is not present. '''
        entry = self._find_entry(key)
        if entry is None:
            raise KeyError
        else: 
            return entry.value

    def rehash(self):
        '''Create a larger bucket table and reinsert all
existing entries using the new table size. '''
        new_list = [[] for i in range(self.size*2)]  # new list containing all buckets 
        for bucket_indx in range(self.size):
            for entry in self._L[bucket_indx]:
                new_ind = hash(entry.key) % (self.size*2)
                new_list[new_ind].append(entry)
        self.size = self.size * 2
        self._L = new_list


