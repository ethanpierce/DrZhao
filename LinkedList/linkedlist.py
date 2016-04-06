# https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Insert: Inserts a new node into the list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Size: returns size of list
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # Search: searches list for a node containing the requeste data and returns that node if found,
    #  otherwise raises an error
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                print "\nFound a Match: " + data + "\n"
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    # Traverse List and print
    # traverse list
    def printList(self):
        current = self.head
        while current:
            print current.get_data()
            current = current.get_next()
        # Delete: searches list for a node containing the requested data and removes it from the list if found,
        #  otherwise raises an error
        # Delete is similar to search. Except we have a previous node that we will keep track of when we remove the node
        # If the head of the list is the node to be removed we set previous to the head in order to remove the element

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                print "\nFound a Match to delete: " + data +"\n"
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            # If we do find the desired element we take the previous node and set the pointer to the found nodes next
            # node pointer
