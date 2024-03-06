
class Stack:
    def __init__(self) -> None:
        self.item = []

    # Method for counting items
    def __len__(self):
        return len(self.item)
    
    # Method for pringting item
    def __str__(self):
        return str(self.item)
    
    #push mehtod
    def push(self,item1):
        self.item.append(item1)

    #pop mehtod
    def pop(self):
        if len(self) == 0:
            return "stack is empty"
        return self.item.pop()
    
    # peek method
    def peek(self):
        return self.item[-1]
    
    # checking is empty
    def is_empty(self):
        return len(self) == 0
    
    # get size
    def size(self):
        return len(self)

#stack = Stack()
#stack.push(23)
#stack.push(65)
#stack.push(623)
#print(stack)
#


if __name__ == "__main__":
    stack = Stack()
    i = True
    while i:
        print("""
                1. Push
                2. Pop
                3. peek
                4. Is empty
                5. Stack Size
                6. Show full stack
                7. Quit program
                \n\n""")
        op = input("Enter operation:  ")
        if op == "1":
            item1 = input("Enter Item : ")
            stack.push(item1)

        elif op == "2":
            stack.pop()

        elif op == "3":
            print(stack.peek())

        elif op == "4":
            print(stack.is_empty())

        elif op == "5":
            print(f" The stack Size is: {stack.size()}")
        elif op == "6":
            print(stack)
        elif op == "7":
            i = False
        else: 
            print("please enter a right operation ")