class InvDict():
    
    def __init__(self, dic=None):
        self.dict       = dict()
        self.inverse    = dict()
        
        if type(dic) != dict and dic != None:
            raise Exception("dic must be of type 'dict'")
            
        if type(dic) == dict:    
            for key, val in dic.getItems():
                dic[key] = val
            
    def clear(self):
        self.dict.clear()
        self.inverse.clear()   
        
    def copy(self):
        dic = self.dict().copy()
        inv = self.inverse().copy()
        
        newInvDict          = InvDict()
        newInvDict.dict     = dic
        newInvDict.inverse  = inv
        
        return newInvDict
        
    def fromkeys(self):
        pass
    
    def get(self, key):
        return self.dict.get(key)
    
    def items(self):
        return self.dict.items()
    
    def keys(self):
        return self.dict.items()
    
    def pop(self, key):
        
        val = self.dict.pop(key)
        self.getInv(val).pop(key)
        
        if len(self.getInv(val))  == 0 :
            self.inverse.pop(val)
        return val
            
    def popitem(self):
        pass
    
    def setdefault(self):
        pass
    
    def update(self):
        pass
    
    def values(self):
        return self.dict.values()
    
    def getInv(self, val):
        return self.inverse[val]
        
    def __setitem__(self, key, val):

        
        #If key is not new
        if key in self.dict:
            
            oldVal = self.dict[key]
            if oldVal == val:
                return
            
            self.dict[key] = val        
            self.getInv(oldVal).pop(key)
            
            if len(self.getInv(oldVal)) == 0:
                self.inverse.pop(oldVal)
                
        #If key is new
        else:
            self.dict[key] = val
        
        #If balue is not new
        #
        #
        #May be better as a tuple
        if val in self.inverse:
            self.getInv(val).append(key)
            
        #If value is new
        else:
            self.inverse[val] = [key]

    def __getitem__(self, key):
        return self.dict[key]


    def __str__(self):
        return self.dict.__str__()
        
        
test = InvDict()

test[1] = 24
test[2] = 41
test[4] = 24

print(test.getInv(24))
print(test)
print(test[1])
print(test.pop(1))
print(test.getInv(24))

print(test.get(2))