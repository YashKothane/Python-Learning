#This is Queue implementation program 
# Queue is very similar to Stack in terms of its structure
# SO there are two ways to implement Queue
    # 1. Using List
    # 2. Using LinkedList

#Also there are two ways in which we can implement Queue using List
    #    1. List methods 
    # 2. using Classes and objects

# so this is the program to implement Queue using Linked List
# Methods in  Queue are Enqueue() Dequeue(), peek() , IsEmpty(), Size()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList():
    def __init__(self):
        self.start=None
    
    def Enqueue(self, data):
        if self.start==None:
            new_node=Node(data)
            self.start=new_node
        else:
            itr=self.start
            new_node=Node(data)
            self.start=new_node
            new_node.next=itr
    
    def Dequeue(self):
        itr=self.start
        temp=itr

        while itr.next!=None:
            temp=itr
            itr=itr.next
        
        temp.next=None
    
    def peek(self):
        itr=self.start

        while itr.next!=None:
            itr=itr.next
        
        print(itr.data)
    
    def IsEmpty(self):
        if self.start!=None:
            return True
        
        else:
            return False
    
    def size(self):
        itr=self.start
        count=1
        while itr.next!=None:
            itr=itr.next
            count=count+1
        
        print(count)
    
    def printer(self):
        itr=self.start
        while itr!=None:
            print(itr.data)
            itr=itr.next

obj1=LinkedList()
obj1.Enqueue(1)
obj1.Enqueue(2)
obj1.Enqueue(3)
obj1.Enqueue(4)
obj1.peek()
obj1.printer()
obj1.Dequeue()
obj1.printer()
obj1.size()
obj1.peek()