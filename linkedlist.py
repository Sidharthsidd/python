"""singly linked list """

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    
    def insert_at_Start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n 
        else:
            self.start=n

    def search(self,data):
        temp=self.start
        while temp is not None :
            if temp.item==data:
                return temp
            temp =temp.next
        return None 
    def print_list(self):
        temp=self.start
        while temp is not None :
            print(temp.item,end=" ")
            temp=temp.next
    def insert_after(self,data,temp):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def delete_first():
        if self.start is not None :
            self.start=self.start.next
    def delete_last ():
        if self.startis None :
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
        def delete_item(self,data):
            temp=self.start
            if self.start is None :
                pass
        elif self.start.next is None :
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            


            



        


#driveing code 

mylist=SLL()
mylist.insert_at_Start(1)
mylist.print_list()
