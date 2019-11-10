class node:
    def __init__(self,val=None,nxt=None):
        self.val=val
        self.nxt=nxt
class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,x,pos):
        temp=node(x)
        temp.nxt=pos.nxt
        pos.nxt=temp
    def append(self,x):
        if self.head==None:
            temp=node(x)
            self.head=temp
            self.tail=temp
        else:
            temp=node(x)
            self.tail.nxt=temp
            self.tail=temp
    def search(self,x):
        cur=self.head
        while cur.nxt != None and cur.val!=x:
            cur=cur.nxt
        if cur.nxt == None and cur.val != x:
            return False
        else:
            return cur
    def print(self):
        cur=self.head
        while cur:
            print(cur.val.task_no)
            cur=cur.nxt
    def findpos(self,x):
        if self.head==None:
            temp=node(x)
            self.head=temp
            self.tail=temp
        else:
            cur=self.head
            if cur.val.cpu>x.cpu:
                new=node(x)
                self.head=new
                new.nxt=cur
                return
            while cur.nxt !=None and cur.nxt.val.cpu<x.cpu:
                cur=cur.nxt
            new=node(x)
            if cur.nxt==None:
                cur.nxt=new
                self.tail=new
                return
            temp=cur.nxt
            cur.nxt=new
            new.nxt=temp


    def rev(self):
        prev=None
        new=None
        cur=self.head.nxt
        while cur:
            new=cur.nxt
            cur.nxt=prev
            prev=cur
            cur=new
        self.head.nxt=prev
        self.print()
    def insert_head(self,x):
        if self.head==None:
            temp=node(x)
            self.head=temp
            self.tail=temp
        else:
            temp=node(x)
            temp.nxt=self.head
            self.head=temp
    def remove(self):
        if self.head==None:
            print("empty")
            return
        if self.head.nxt==None:
            temp=self.head
            self.head=None
            self.tail=None
            return temp
        else:
            temp=self.head
            self.head=self.head.nxt
            temp.nxt=None
            return temp
            
            


def main():
    l=linked_list()
    '''l.insert_head(8)
    l.insert_head(6)
    l.insert_head(5)'''
    l.insert_head(1)
    l.findpos(3)
    l.print()
    print("tail",l.tail.val)
    l.remove()
    l.remove()
    l.remove()
    l.remove()
    l.remove()

if __name__=="__main__":
    main()
            
            
    
    
