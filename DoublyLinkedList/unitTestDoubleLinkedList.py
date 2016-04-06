from DoublyList import DoubleLinkedList

def main():
    # Create list of names
    listOfNames = {"Tom", "Harry", "Susan", "Ethan", "Willy", "Shaina"}

    #Create DoublyLinkedList Object
    testDoubleLinkedList = DoubleLinkedList()

    #Test Insertion method
    for name in listOfNames:
        testDoubleLinkedList.insert(name)

    #print size
    print testDoubleLinkedList.size()

    #print list forwards
    testDoubleLinkedList.printForward()

    #print list backwards
    print "\n"
    testDoubleLinkedList.printBackwards()




if __name__ == '__main__':
    main()
