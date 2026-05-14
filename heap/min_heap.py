class MinHeap:
    def __init__(self):
        self.__heap = []
        
    def __iter__(self):
        print("__iter__")
        return self
    
    def _get_parent_index(self,index):
        return (index - 1) // 2
    
    def _get_left_child_index(self, index):
        return (2 * index) + 1
    
    def _get_right_child_index(self,index):
        return (2 * index) + 2
    
    def _swap(self,index1 , index2):
        self.__heap[index1], self.__heap[index2] = self.__heap[index2], self.__heap[index1]
        
    # def _bubble_up(self,index):
    #     parent = self._get_parent_index(index)
    #     if index > 0 and self.__heap[index] > self.__heap[parent]:
            
    # def insert(self,value):
    #     self.__heap.append(value)
    
        
        
        
        