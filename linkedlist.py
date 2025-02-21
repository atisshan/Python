class Node:
    def __init__(self, data=None):
        self.next=None
        self.data=data
class LL:
    def __init__(self):
        self.head=Node()

    def print_ll(self,data):
        if self.head is  None:
            print("Empty list")
        else:
            cur_node=self.head
            new_node=Node(data)
            while cur_node.next != None:
                cur_node=cur_node.next
            cur_node=new_node

    def display(self):
        elem=[1,2,3,4]
        cur=self.head
        while cur.next is not None:
           cur=cur.next
           elem.append(cur.data)
            
        print(elem)

    def length(self):
        cur_node = self.head
        
        elem=[1,2,3,4]
        total=0
        while cur_node.next is not None:
           total +=1
           cur_node=cur_node.next
           
        print(total)
            



            
        
            
       


ll1=LL()

ll1.length()





