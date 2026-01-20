class Stack: # Defining the Stack class.
    def __init__(self): # Defining the constructor function.
        # print("alahuakibar")
        self.__stack_list = []
    
    
    def push(self,value): # Add a value into stack
        self.__stack_list.append(value)
        
    def pop(self): # Remove the item in the top of the stack
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value
    
    def show_stack(self):
        print(self.__stack_list)


if __name__ == "__main__":
    stack_object = Stack()  # Instantiating the object.
    
    stack_object.push(1)
    stack_object.push(5)
    stack_object.push(7)
    
    stack_object.show_stack()
    
    print(stack_object.pop())
    
    stack_object.show_stack()
    print(stack_object.__dict__)
    
    