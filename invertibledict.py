
class InvDict():
    '''
    Invertible dictionary
    Can be used as a regular dictionary
    Additional getinv(val) method: 
        - Returns a tuple of all keys which have a value of val
    '''
    def __init__(self, iterable=None):
        self._dict       = dict()
        self._inverse    = dict()
        
        if iterable == None:
            return
            
        for key, val in iterable:
            self[key] = val
            
    def clear(self):
        self._dict.clear()
        self._inverse.clear()   
        
    def copy(self):
        dic = self._dict().copy()
        inv = self._inverse().copy()
        
        newInvDict          = InvDict()
        newInvDict._dict    = dic
        newInvDict._inverse = inv
        
        return newInvDict
        
    def fromkeys(self, sequence, val=None):
        for key in sequence:
            self[key] = val
    
    def get(self, key):
        return self._dict.get(key)
    
    def items(self):
        return self._dict.items()
    
    def keys(self):
        return self._dict.items()
    
    def pop(self, key):
        
        val = self._dict.pop(key)
        self._inverse[val].pop(key)
        
        if len(self.getinv(val))  == 0 :
            self._inverse.pop(val)
        return val
            
    def popitem(self):
        key, val = self._dict.popitem()
        self._inverse[val].remove(key)
            
        return val;
    
    def setdefault(self, key, defaultValue=None):
        if key not in self._dict:
            self[key] = defaultValue
            
    def update(self, iterable):
        if type(iterable) == dict:
            for key, val in iterable.items():
                self[key] = val
                
        else:
            for key, val in iterable:
                self[key] = val
    
    def values(self):
        return self._dict.values()
    
    def getinv(self, val):
        '''
        Returns a tuple of all keys which have a value of 'val'
        '''
        return tuple(self._inverse[val])
        
    def __setitem__(self, key, val):
        
        #If key is not new
        if key in self._dict:
            
            oldVal = self._dict[key]
            if oldVal == val:
                return
            
            self._dict[key] = val        
            self._inverse[oldVal].remove(key)
            
            if len(self.getinv(oldVal)) == 0:
                self._inverse.pop(oldVal)
                
        #If key is new
        else:
            self._dict[key] = val

        #If value is not new
        if val in self.inverse:
            self.inverse[val].append(key)

        #If value is new
        else:
            self.inverse[val] = [key]
            
    def __iter__(self):
        return self._dict.__iter__()

    def __getitem__(self, key):
        return self._dict[key]

    def __str__(self):
        return self._dict.__str__()
