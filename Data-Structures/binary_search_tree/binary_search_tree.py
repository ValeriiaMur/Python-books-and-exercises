"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #RECURSIVE PLAN
        #if value < root
        #if left child is none
                #add here
            #else
        #if value >= root(dupes to right)
            #if right child is none
                #add here
            #else
                #recursive call
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

        
    #ITERATIVE PLAN
    #while not at the botttom, keep going
        #go left
            #if the left child is none, 
                # add here
                #exit loop
            
        #go right, same values go right too
            #if right child is none 
                #add here
                #exit loop


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is target:
            return True
        elif self.right == None and self.left == None:
            return False
        elif self.value > target:
            return self.left.contains(target)
        else:
            return self.right.contains(target)
        # else:
        #     #go left
        #     if target < self.value:
        #         if self.left is target:
        #             return True
        #         else:
        #             self.contains(target)

        #     #go right
        #     elif target >= self.value:
        #         if self.right is target:
        #             return True
        #         else:
        #             self.contains(target)
        #     return False

    # Return the maximum value found in the tree
    def get_max(self):
        #go right until you cannot, return max
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #one side than other
        #call fun(value)
        fn(self.value)

        #base
        if self.left is None and self.right is None:
            return

        #Recursive
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        nodes = []
        nodes.push(self.value)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

    def in_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
