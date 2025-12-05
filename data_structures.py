import social_media as sm
# Doney Tran
# 11/22/25
# CS302
# Program 4-5

class Node234():
    def __init__(self, data=None):
        # Default empty list = empty 234 node, if data is passed in, then fill in the 0th index with data which makes it 
        # a 234 node with 1 data inside it
        self.__data: list = [] 
        if data:
            self.__data.append(data)

        self.__child: list = [None, None, None, None] 

    # This functions loops through the list and displays if there is a social media object in it. 
    def display(self):
        for data in self.__data:
            data.display()

    # Since comparison is overloaded with social media, sort should work, pretty neat
    # insert sorted
    def insert(self, data) -> int:
        self.__data.append(data)
        self.__data.sort()

    # Getter functions since the data list is private, can access it since it's python, but going to keep it consistent
    def get_child(self, index: int):
        return self.__child[index]
    
    def get_data(self, index: int) -> list:
        return self.__data[index]

    def get_data_length(self) -> int:
        return len(self.__data) 

    # Setter functions since the data list is private.
    def set_child(self, index: int, node):
        self.__child[index] = node

    def set_data(self, index: int, data):
        self.__data[index] = data 

    # Boolean operations 
    # This function checks to see if a node is a leaf. It will be used to determine where to insert. It returns True if all
    # the children of the node is None. Otherwise it will return False.
    def is_leaf(self) -> bool:
        if self.__child[0] == None and self.__child[1] == None and self.__child[2] == None and self.__child[3] == None:
            return True
        return False

    # This function checks if the list of a node is full which should contain 3 social media objects. It will return True if there is 3,
    # otherwise it will return False. 
    def is_full(self) -> bool:
        return len(self.__data) == 3
    


class Tree234():
    # Default constructor
    def __init__(self):
        self.__root: Node234 = None

    # This is a wrapper function to check if the root is None. If it is, a message will be displayed saying
    # that it is empty. Otherwise the function will call the recursive display function.
    def display(self):
        if self.__root == None:
            print("Nothing to display. the 2-3-4 tree is empty.")
            return

        return self.__display(self.__root)

    # This is a wrapper function to insert into the 234 tree. If there is no root, then a new 234 node will be
    # created and data is added. It also checks to see if the root node is full and will split it. Otherwise the function
    # will call it's recursive insert function.
    def insert(self, data):
        if self.__root == None:
            self.__root = Node234(data)
            return

        # If root is full, we split the root
        if self.__root.is_full():
            # Hold the old root before splitting
            old_root = self.__root
            self.__root = Node234()
            self.__root.set_child(0, old_root)
            self._split_child(self.__root, 0)

        self._insert(self.__root, data)

    
    # Protected functions
    # This function is used in insert to split a full node whenever one is encountered in the tree.
    def _split_child(self, parent: Node234, index: int):
        node_to_split = parent.get_child(index)
        middle = node_to_split.get_data(1)

        # Create a new left and right node for middle to link up to. Ex 20, 30, 40, when I want to insert 50
        # 30 is pushed up, and to the left is 20, the right is 40.
        #    30
        #   /  \
        #  20  40
        left: Node234 = Node234(node_to_split.get_data(0))
        right: Node234 = Node234(node_to_split.get_data(2))

        # Making sure if the node to split has children that we rearrange them
        if not node_to_split.is_leaf():
            left.set_child(0, node_to_split.get_child(0))
            left.set_child(1, node_to_split.get_child(1))
            right.set_child(0, node_to_split.get_child(2))
            right.set_child(1, node_to_split.get_child(3))

        # Pushing the middle data we just split to parent, and rearranging the parents children to the new split
        parent.insert(middle)
        parent.set_child(index, left)
        parent.set_child(index + 1, right)

    # Private functions
    # Recursive functions
    # This function recursively traverses through the nodes to display all the social media objects in the tree. It
    # will display the userID inorder by the character length of the userID.
    def __display(self, node: Node234):
        if node == None:
            return

        # Ex tree so tracing through is easier to follow
        #               20, 30, 40    <---- node
        #              /   |   |   \ 
        #          15, 16  25  32   41, 100, 105

        # Get the length in whatever node we are in which is 3.
        total_data: int = node.get_data_length()
        
        # Go inside the loop then recursively call display on a child 
        # until we hit the base case then display.
        # call into the 15,16 node, it has total_data of 2, again hit the base case but its null, so we go back to the
        # 15, increment the index, then display 16, and then we return back up to the starting for loop and print 20
        # rinse and repeat. I don't know if that made any sense :\
        for index in range(total_data):
            self.__display(node.get_child(index))
            node.get_data(index).display()

        # Special case handling the last child
        self.__display(node.get_child(total_data))


    # This recursive function checks to see if the data to be inserted meets certain conditions. The conditions are listed below
    # through comments. In a 234 tree, we split first if we encounter a full node, then traverse through to insert. I think there 
    # are other orders that you can do, but I stuck to what showed up from videos and the internet.
    def _insert(self, node: Node234, data):
        # Base case
        if node == None:
            return

        # Inserting into a node that is a leaf
        if node.is_leaf():
            node.insert(data)

        # Splitting node
        else:
            index: int = 0

            # Possible with overloadeded social media operator
            # iterate to get to the correct child to insert in
            while index < node.get_data_length() and data > node.get_data(index):
                index += 1

            child = node.get_child(index)
            
            # We encounter a full node and split
            if child and child.is_full():
                self._split_child(node, index)

                # After split, find the right index to insert key into since the split moved things around
                if data > node.get_data(index):
                    index += 1

            self._insert(node.get_child(index), data)
