class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #set next_node of my new node to the head
            new_node.set_next_node(self.head)
            #update head
            self.head = new_node
        

    def add_to_tail(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        #empty list
        if self.head is None:
            return None
        else:
            return_val = self.head.get_value()
            #one thing
            if self.head == self.tail:
                self.head = None
                self.tail = None
            #nonempty - return a VALUE of the old head
            else:
                self.head = self.head.get_next_node()
            return return_val


    def remove_tail(self):
        if(self.head is None):
            return None
        if self.head.next_node is None:
            self.head = None
            return None
        second_last = self.head
        while(second_last.next_node.next_node):
            second_last = second_last.next_node
        second_last.next_node = None
        return self.head.value

    def contains(self,value):
        pass

    def get_max(self):
        pass