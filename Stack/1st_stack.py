class stack:
    def push(self,n):
        stack_list.append(n)
        return stack_list
    def pop(self):
        if len(stack_list)>1 or len(stack_list) ==0:
            print("Stack empty")
        else:
            stack_list.pop()

stack_list = []
obj1 = stack()
how = int(input("How many data do you want to entry: "))
for i in range ( how ):
    try:
        value = float(input("Enter your data "))
    except ValueError:
        print("Please Enter integer or float data")
    obj1.push(value)

print(stack_list)

n = input("Do you want to pop data: yes/no: ")
if n=="yes":
    try:
        pop_data = int(input("How many data do you want to pop : "))
    except ValueError:
        print("Please enter intger value")
    if pop_data<len(stack_list):
        obj1.pop()
    else:
        print ("You can not pop more than the length of list.")
print(stack_list)
