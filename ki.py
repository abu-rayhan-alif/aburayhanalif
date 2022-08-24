
class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __int__(self):
        self.head=None

    def tra(self):
        if self.head is None:
            print("Print empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next

n1=Node(8)
l=LinkedList()
l.head=n1
n2=Node(3)
n1.next=n2
n3=Node(5)
n2.next=n3
l.tra()

