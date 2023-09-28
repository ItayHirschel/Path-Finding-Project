class MinHeap:
    def __init__(self):
        self.collection = []
        self.valueDict = {}
    
    def clear(self):
        self.collection = []
        self.valueDict = {}


    def bubbleUp(self, index):
        if index >= len(self.collection) :
            print("Somehow error")
            return
        
        p_index = self.parentIndex(index)
        if (0 > p_index):
            return
        
        # Switch values if child < parent
        child_val = self.valueDict[self.collection[index]]
        parent_val = self.valueDict[self.collection[p_index]]
        if (child_val < parent_val):
            temp = self.collection[p_index]
            self.collection[p_index] = self.collection[index]
            self.collection[index] = temp
        
        self.bubbleUp(p_index)

    
    def bubbleDown(self, index = 0):
        
        if self.isEmpty():
            return
        
        children = self.indexChildren(index)

        parent_val = self.valueDict[self.collection[index]]

        if children[0] >= len(self.collection):
            return
        
        left_child_val = self.valueDict[self.collection[children[0]]]
        
        if children[1] >= len(self.collection):
            if (parent_val > left_child_val):
                temp = self.collection[children[0]]
                self.collection[children[0]] = self.collection[index]
                self.collection[index] = temp
                self.bubbleDown(children[0])
            return
         
        right_child_val = self.valueDict[self.collection[children[1]]]
            
        if (parent_val > right_child_val and parent_val > left_child_val):
            if (left_child_val < right_child_val):
                temp = self.collection[children[0]]
                self.collection[children[0]] = self.collection[index]
                self.collection[index] = temp
                self.bubbleDown(children[0])
            else:
                temp = self.collection[children[1]]
                self.collection[children[1]] = self.collection[index]
                self.collection[index] = temp
                self.bubbleDown(children[1])
                
        
        elif parent_val > right_child_val:
            temp = self.collection[children[1]]
            self.collection[children[1]] = self.collection[index]
            self.collection[index] = temp
            self.bubbleDown(children[1])
            return
        
        elif parent_val > left_child_val:
            temp = self.collection[children[0]]
            self.collection[children[0]] = self.collection[index]
            self.collection[index] = temp
            self.bubbleDown(children[0])
            return

    
    def push(self, key, value):
        self.collection.append(key)
        self.valueDict[key] = value
        self.bubbleUp(len(self.collection) - 1)
    
    def pop(self):
        if (len(self.collection) == 0):
            return None
        
        
        key = self.collection[0]

        self.collection[0] = self.collection[-1]
        value = self.valueDict.pop(key)
        self.collection.pop()

        self.bubbleDown()

        return key, value
    
    def contains(self, element):
        return element in self.collection
    
    def decrease(self, key, new_value):

        if new_value >= self.valueDict[key]:
            return False
        
        self.valueDict[key] = new_value
        self.bubbleUp(self.collection.index(key))
        return True

    
    def indexChildren(self, index):
        l_child = index * 2 + 1
        r_child = index * 2 + 2
        return (l_child, r_child)

    
    def parentIndex(self,index):
        if 0 == index:
            return -1
        return int((index - 1) // 2)

    
    def log2cieling(self, value):
        x = 1
        i = 0
        while x < value:
            x *= 2
            i += 1
        return i
    
    def whatLevel(self, index):
        depth = 0
        while index > 0 :
            depth += 1
            index = self.parentIndex(index)
        return depth
    
    def isEmpty(self):
        if len(self.collection) == 0:
            return True
        return False
