class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head

        self.head=new_node
    def search(self,x):
        current=self.head

        while current is not None:
            if current.data == x:
                return True
            current=current.next

        return False
    def counting(self):
        temp=self.head
        count = 0

        while temp:
            count+=1
        temp = temp.next
        print(count)       
if __name__ == '__main__':

    ll1=LinkedList()
    x = 21

    ll1.push(10)
    ll1.push(14)
    ll1.push(11)
    ll1.push(20)
    ll1.push(21)

    if ll1.search(x):
        print('true')
    else:
        print("False")
    ll1.counting()
