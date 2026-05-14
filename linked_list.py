#Linked list is when an item on the list points to another item called node
#Searching from a linked list is O(n) but insertion is O(1)
#creating a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #declare .next as None
#Creating a liked list
class LinkedList:
    def __init__(self):
        self.head = None #declare head as None (empty list)

    def append(self,data):
        new_node = Node(data) #the new Input
        if self.head is None: #head is None, meaning the list is empty
            self.head = new_node #make the head None into the input
        else:#if the list is not empty
            current = self.head #current head value is stored in current
            while current.next is not None:#loop until current value reaches None = end of the list
                current = current.next# move current value to the next node
            current.next = new_node #attach new value to end of list

    #to print the list
    def print_list(self):
        current = self.head #assign first value to current
        while current is not None: #loop until it reaches the end of loop
            print(current.data, end="->") #print current.data #end is a parameter of print(). print() automatically adds \n
            current = current.next #current value becomes the next value
        print("None")#after all actual data, print None at last

    #to attach data to the start of the list
    def prepend(self,data):
        new_node = Node(data) #new node is the new input
        new_node.next = self.head #new node's next item is the head(any value)
        self.head = new_node #the head value is assigned to the new node

    def delete(self, data):
        current = self.head #assign head value to current
        previous = None #initiate previous to traverse to the index-1 position
        #to check if the deletion is in the head, if so, remove the head
        if current.data ==data: #if the input is equal to input data
            self.head = current.next #heading becomes the next value of current
        #if it's any other item, the node is deleted and the position is reassigned to point correctly
        else:
            while current is not None: #till current reaches last potision
                if current.data == data: #if the current data is the same as input
                    previous.next = current.next #the next item from previous becomes the current value (replace)
                    return #end here if condition met
                previous = current #replace the previous value with current till the end
                current = current.next #current value becomes its next value

my_list = LinkedList()
my_list.append(1)
my_list.append(3)
my_list.append(6)
my_list.prepend(4)
my_list.delete(6)
my_list.print_list()
#Output 4->1->3->None