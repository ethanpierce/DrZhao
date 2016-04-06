class Node(object):
    def __init__(self,data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def set_next(self,new_next):
        self.next = new_next
    def set_prev(self,new_prev):
        self.prev = new_prev

class DoubleLinkedList(object):
    def __init__(self,head = None, tail = None):
        self.head = head
        self.tail = tail
    #Insert
    def insert(self,data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            self.tail = self.head
        else:
            #set current head to point to new node as it will now
            #  be a previous node
            self.head.set_prev(new_node)

            #Set new node to point to current head
            new_node.set_next(self.head)

            #set new node as new head
            self.head = new_node


    #Size
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    #Search
    #def search(self,data):

    #Delete
    def delete(self,data):
        current = self.head
        found = False
        while current:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        else:
            current.get_prev(current.set_next())
            current.get_next(current.set_prev())
    #Print Forward
    def printForward(self):
        current = self.head

        if current == None:
            raise ValueError("List is Empty")

        while current:
            print current.get_data()
            current = current.get_next()
    #Print Backwrads
    def printBackwards(self):
        current = self.tail

        if current == None:
            raise ValueError("List is Empty")

        while current:
            print current.get_data()
            current = current.get_prev()
