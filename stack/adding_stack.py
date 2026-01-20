from stack import Stack

class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0
        
    def push(self,value):
        self.__sum += value
        super().push(value)
        
    def pop(self):
        value  = super().pop()
        self.__sum -= value
        return value
    
    def get_sum(self):
        return self.__sum
    
    
    
if __name__ == "__main__":
    stack_object = AddingStack()  # Instantiating the object.
    
    stack_object.push(1)
    stack_object.push(5)
    stack_object.push(7)
    
    stack_object.show_stack()
    
    print(stack_object.pop())
    
    stack_object.show_stack()
    print(stack_object.get_sum())
    print(stack_object.__dict__)