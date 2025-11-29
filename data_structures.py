import hierarchy
# Doney Tran
# 11/22/25
# CS302
# Program 4-5


class NodeRB():
    def __init__(self, data=None, left=None, right=None, color = True):
        self.__data: hierarchy.SocialMedia = data
        self.__left: NodeRB = left
        self.__right: NodeRB = right
        # Red is True, Black is false
        self.__color: bool = color
        self.__parent: NodeRB = None

    # Getters
    def get_left(self):
        return self.__left 

    def get_right(self):
        return self.__right

    def get_data(self):
        return self.__data

    # Setters
    def set_left(self, node):
        self.__left = node
    
    def set_right(self, node):
        self.__right = node

    def set_parent(self, node):
        self.__parent = node

    def set_red(self):
        self.__color = True

    def set_black(self):
        self.__color = False

        

class RBTree():
    def __init__(self, root: NodeRB=None):
        self.__root: NodeRB = root

    def __fix(self, node: NodeRB):
        pass

    def __insert(self,node: NodeRB, data: hierarchy.SocialMedia) -> NodeRB:    
        pass

    def insert(self, data):
        pass
    
    # Display inorder
    def display(self):
        pass

    def search(self, name: str):
        pass


