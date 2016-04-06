from linkedlist import LinkedList



def main():
    #Create list of names
    listOfNames = { "Tom", "Harry","Susan","Ethan","Willy","Shaina"}

    #Create linkedlist object
    testinglist = LinkedList()

    #Test insertion method
    for name in listOfNames:
        testinglist.insert(name)

    #Test size of list
    print testinglist.size()

    #Test print list
    testinglist.printList()

    #Test Deletion of head node
    testinglist.delete("Tom")

    #Test Deletion method:
    testinglist.delete("Susan")
    testinglist.printList()

    #Test search list
    testinglist.search("Willy")


if __name__ == '__main__':
    main()