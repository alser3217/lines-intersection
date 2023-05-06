from AVLTree import *
from bisect import bisect_left

class B_2_3Node():

    def __init__(self, value, first = None, second = None, third = None, fourth = None, parent = None):

        self.size = 1
        self.parent = parent
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.keys = [None] * 3
        self.keys[0] = value

    def __str__(self):
        return(f'({self.keys[0]}, {self.keys[1]})')

    def find(self, value):

        for i in range(self.size):
            if self.keys[i] == value:
                return True
        return False

    def insert_to_node(self, value):

        self.keys[self.size] = value
        self.size += 1
        if self.size == 1:
            return
        elif self.size == 2:
            if self.keys[0] > self.keys[1]:
                tmp = self.keys[0]
                self.keys[0] = self.keys[1]
                self.keys[1] = tmp
        else:
            self.keys.sort()

    def remove_from_node(self, value):

        if self.size >= 1 and self.keys[0] == value:
            self.keys[0] = self.keys[1]
            self.keys[1] = self.keys[2]
            self.size -= 1
        elif self.size == 2 and self.keys[1] == value:
            self.keys[1] = self.keys[2]
            self.size -= 1

    def become_node2(self, value, first, second):

        self.keys[0] = value
        self.keys[1] = None
        self.keys[2] = None
        self.first = first
        self.second = second
        self.third = None
        self.fourth = None
        self.parent = None
        self.size = 1

    def is_leaf(self):

        return self.first == None and self.second == None and self.third == None
    
class B_2_3Tree():

    def insert(self, node, value):

        if not node:
            return B_2_3Node(value)

        if node.is_leaf():
            node.insert_to_node(value)
        elif value < node.keys[0]:
            self.insert(node.first, value)
        elif node.size == 1 or (node.size == 2 and value <= node.keys[1]):
            self.insert(node.second, value)
        else:
            self.insert(node.third, value)

        return self.split(node)

    def split(self, node):

        if node.size < 3:
            return node
        
        x = B_2_3Node(node.keys[0], node.first, node.second, None, None, node.parent)
        y = B_2_3Node(node.keys[2], node.third, node.fourth, None, None, node.parent)

        if x.first:
            x.first.parent = x
        if x.second:
            x.second.parent = x
        if y.first:
            y.first.parent = y
        if y.second:
            y.second.parent = y
        
        if node.parent:
            node.parent.insert_to_node(node.keys[1])

            if node.parent.first == node:
                node.parent.first = None
            elif node.parent.second == node:
                node.parent.second = None
            elif node.parent.third == node:
                node.parent.third = None

            if not node.parent.first:
                node.parent.fourth = node.parent.third
                node.parent.third = node.parent.second
                node.parent.second = y
                node.parent.first = x
            elif not node.parent.second:
                node.parent.fourth = node.parent.third
                node.parent.third = y
                node.parent.second = x
            else:
                node.parent.fourth = y
                node.parent.third = x

            tmp = node.parent
            return tmp

        else:
            x.parent = node
            y.parent = node
            node.become_node2(node.keys[1], x, y)
            return node

    def search(self, node, value):

        if not node:
            return

        if node.find(value):
            return node
        elif value < node.keys[0]:
            return self.search(node.first, value)
        elif node.size == 1 or node.size == 2 and value < node.keys[1]:
            return self.search(node.second, value)
        else:
            return self.search(node.third, value)     

    def search_min(self, node):

        if node:
            while node.first:
                node = node.first
            
        return node

    def next(self, node, value):

        parent = node.parent

        if not parent and node.is_leaf():
            if node.size == 2 and node.keys[0] == value:
                return node.keys[1]
            else:
                return None

        if node.is_leaf():
            if parent.size == 2:
                if node == parent.first:
                    if node.size == 2:
                        if node.keys[0] == value:
                            return node.keys[1]
                        else:
                            return parent.keys[0]
                    else:
                        return parent.keys[0]
                elif node == parent.second:
                    if node.size == 2:
                        if node.keys[0] == value:
                            return node.keys[1]
                        else:
                            return parent.keys[1]
                    else:
                        return parent.keys[1]
                else:
                    if node.size == 2:
                        if node.keys[0] == value:
                            return node.keys[1]
                        else:
                            current_node = node
                            while parent and current_node == parent.third:
                                current_node = parent
                                parent = parent.parent
                            if parent:
                                return parent.keys[0]
                            else:
                                return None

            else:
                if node == parent.first:
                    if node.size == 2:
                        if node.keys[0] == value:
                            return node.keys[1]
                        else:
                            return parent.keys[0]
                    else:
                        return parent.keys[0]
                    
                else:
                    if node.size == 2:
                        if node.keys[0] == value:
                            return node.keys[1]
                    else:
                        current_node = node
                        while parent and current_node == parent.second:
                            current_node = parent
                            parent = parent.parent
                        if parent:
                            return parent.keys[0]
                        else:
                            return None
        else:
            if node.size == 2:
                if node.keys[0] == value:
                    current_node = node.second
                    while current_node.first:
                      current_node = current_node.first
                    return current_node.keys[0]
                else:
                    current_node = node.third
                    while current_node.first:
                      current_node = current_node.first
                    return current_node.keys[0]

            else:
                current_node = node.second
                while current_node.first:
                    current_node = current_node.first
                return current_node.keys[0]

    def previous(self, node, value):

        parent = node.parent

        if not parent and node.is_leaf():
            if node.size == 2 and node.keys[1] == value:
                return node.keys[0]
            else:
                return None

        if node.is_leaf():
            if parent.size == 2:
                if node == parent.first:
                    if node.size == 2:
                        if node.keys[1] == value:
                            return node.keys[0]
                        else:
                            current_node = node
                            while parent and current_node == parent.first:
                                current_node = parent
                                parent = parent.parent
                            if parent:
                                return parent.keys[0]
                            else:
                                return None 
                    else:
                        current_node = node
                        while parent and current_node == parent.first:
                            current_node = parent
                            parent = parent.parent
                        if parent:
                            return parent.keys[0]
                        else:
                            return None            
                elif node == parent.second:
                    if node.size == 2:
                        if node.keys[1] == value:
                            return node.keys[0]
                    else:
                        return parent.keys[0]
                else:
                    if node.size == 2:
                        if node.keys[1] == value:
                            return node.keys[0]
                        else:
                            return parent.keys[1]
                    else:
                        return parent.keys[1]
            else:
                if node == parent.first:
                    if node.size == 2:
                        if node.keys[0] == value:
                            current_node = node
                            while parent and current_node == parent.first:
                                current_node = parent
                                parent = parent.parent
                            if parent:
                                return parent.keys[0]
                            else:
                                return None
                        else:
                            return node.keys[0]
                    else:
                        current_node = node
                        while parent and current_node == parent.first:
                            current_node = parent
                            parent = parent.parent
                        if parent:
                            return parent.keys[0]
                        else:
                            return None
                elif node == parent.second:
                    if node.size == 2:
                        if node.keys[1] == value:
                            return node.keys[0]
                        else:
                            return parent.keys[0]
                    else:
                        return parent.keys[0]
        else:
            if node.size == 2:
                if node.keys[1] == value:
                    current_node = node.second
                    while current_node:
                        if current_node.third:
                            current_node = current_node.third
                        elif current_node.second:
                            current_node = current_node.second
                        else:
                            break
                    if current_node.keys[1]:
                        return current_node.keys[1]
                    else:
                        return current_node.keys[0]
                
                else:
                    current_node = node.first
                    while current_node:
                        if current_node.third:
                            current_node = current_node.third
                        elif current_node.second:
                            current_node = current_node.second
                        else:
                            break
                    if current_node.keys[1]:
                        return current_node.keys[1]
                    else:
                        return current_node.keys[0]
            else:
                current_node = node.first
                while current_node:
                    if current_node.third:
                        current_node = current_node.third
                    elif current_node.second:
                        current_node = current_node.second
                    else:
                        break
                if current_node.keys[1]:
                    return current_node.keys[1]
                else:
                    return current_node.keys[0]

    def delete(self, node, value):

        item = self.search(node, value)

        if not item:
            return node

        if item.keys[0] == value:
            min = self.search_min(item.second)
        else:
            min = self.search_min(item.third)

        if min:
            if value == item.keys[0]:
                tmp = item.keys[0]
                item.keys[0] = min.keys[0]
                min.keys[0] = tmp
            else:
                tmp = item.keys[1]
                item.keys[1] = min.keys[0]
                min.keys[0] = tmp

            item = min

        item.remove_from_node(value)

        return self.fix(item)

    def redistribute(self, node):

        parent = node.parent
        first = parent.first
        second = parent.second
        third = parent.third

        if parent.size == 2 and first.size < 2 and second.size < 2 and third.size < 2:
            if first == node:
                parent.first = parent.second
                parent.second = parent.third
                parent.third = None
                parent.first.insert_to_node(parent.keys[0])
                parent.first.third = parent.first.second
                parent.first.second = parent.first.first

                if node.first:
                    parent.first.first = node.first
                elif node.second:
                    parent.first.first = node.second

                if parent.first.first:
                    parent.first.first.parent = parent.first

                parent.remove_from_node(parent.keys[0])
                first = None
            elif second == node:
                first.insert_to_node(parent.keys[0])
                parent.remove_from_node(parent.keys[0])
                if node.first:
                    first.third = node.first
                elif node.second:
                    first.third = node.second

                if first.third:
                    first.third.parent = first

                parent.second = parent.third
                parent.third = None

                second = None 

            elif third == node:
                second.insert_to_node(parent.keys[1])
                parent.third = None
                parent.remove_from_node(parent.keys[1])
                if node.first:
                    second.third = node.first
                elif node.second:
                    second.third = node.second

                if second.third:
                    second.third.parent = second

                third = None

        elif parent.size == 2 and ((first != None and first.size == 2) or (second != None and second.size == 2) or (third != None and third.size == 2)):
            if third == node:
                if node.first:
                    node.second = node.first
                    node.first = None
                node.insert_to_node(parent.keys[1])
                if second.size == 2:
                    parent.keys[1] = second.keys[1]
                    second.remove_from_node(second.keys[1])
                    node.first = second.third
                    second.third = None
                    if node.first:
                        node.first.parent = node
                elif first.size == 2:
                    parent.keys[1] = second.keys[0]
                    node.first = second.second
                    second.second = second.first
                    if node.first:
                        node.first.parent = node

                    second.keys[0] = parent.keys[0]
                    parent.keys[0] = first.keys[1]
                    first.remove_from_node(first.keys[1])
                    second.first = first.third
                    if second.first:
                        second.first.parent = second
                    first.third = None

            elif second == node:
                if third.size == 2:
                    if not node.first:
                        node.first = node.second
                        node.second = None
                    
                    second.insert_to_node(parent.keys[1])
                    parent.keys[1] = third.keys[0]
                    third.remove_from_node(third.keys[0])
                    second.second = third.first
                    if second.second:
                        second.second.parent = second

                    third.first = third.second
                    third.second = third.third
                    third.third = None
                elif first.size == 2:
                    if not node.second:
                        node.second = node.first
                        node.first = None

                    second.insert_to_node(parent.keys[0])
                    parent.keys[0] = first.keys[1]
                    first.remove_from_node(first.keys[1])
                    second.first = first.third
                    if second.first:
                        second.first.parent = second

                    first.third = None

            elif first == node:
                if not node.first:
                    node.first = node.second
                    node.second = None
                
                first.insert_to_node(parent.keys[0])
                if second.size == 2:
                    parent.keys[0] = second.keys[0]
                    second.remove_from_node(second.keys[0])
                    first.second = second.first
                    if first.second:
                        first.second.parent = first

                    second.first = second.second
                    second.second = second.third
                    second.third = None

                elif third.size == 2:
                    parent.keys[0] = second.keys[0]
                    second.keys[0] = parent.keys[1]
                    parent.keys[1] = third.keys[0]
                    third.remove_from_node(third.keys[0])
                    first.second = second.first
                    if first.second:
                        first.second.parent = first
                    second.first = second.second
                    second.second = third.first
                    if second.second:
                        second.second.parent = second
                    third.first = third.second
                    third.second = third.third
                    third.third = None

        elif parent.size == 1:
            node.insert_to_node(parent.keys[0])

            if first == node and second.size == 2:
                parent.keys[0] = second.keys[0]
                second.remove_from_node(second.keys[0])
                if not node.first:
                    node.first = node.second

                node.second = second.first
                second.first = second.second
                second.second = second.third
                second.third = None
                if node.second:
                    node.second.parent = node

            elif second == node and first.size == 2:
                parent.keys[0] = first.keys[1]
                first.remove_from_node(first.keys[1])
                if not node.second:
                    node.second = node.first

                node.first = first.third
                first.third = None
                if node.first:
                    node.first.parent = node
                
        return parent

    def merge(self, node):

        parent = node.parent

        if parent.first == node:
            parent.second.insert_to_node(parent.keys[0])
            parent.second.third = parent.second.second
            parent.second.second = parent.second.first

            if node.first:
                parent.second.first = node.first
            elif node.second:
                parent.second.first = node.second

            if parent.second.first:
                parent.second.first.parent = parent.second

            parent.remove_from_node(parent.keys[0])
            parent.first = None

        elif parent.second == node:
            parent.first.insert_to_node(parent.keys[0])

            if node.first:
                parent.first.third = node.first
            elif node.second:
                parent.first.third = node.second

            if parent.first.third:
                parent.first.third.parent = parent.first

            parent.remove_from_node(parent.keys[0])
            parent.second = None

        if not parent.parent:
            if parent.first:
                tmp = parent.first
            else:
                tmp = parent.second

            tmp.parent = None
            parent = None
            
            return tmp
        
        return parent
                        
    def fix(self, node):
        
        if node.size == 0 and not node.parent:
            return None
        if node.size != 0:
            if node.parent:
                return self.fix(node.parent)
            else:
                return node 

        parent = node.parent
        if parent.first.size == 2 or parent.second.size == 2 or parent.size == 2:
            node = self.redistribute(node)
        elif parent.size == 2 and parent.third.size == 2:
            node = self.redistribute(node)
        else:
            node = self.merge(node)
        return self.fix(node)
    
    def DFS_traversal(self, node):

        if not node:
            return
    
        print(node.keys[0], node.keys[1]) 
        self.DFS_traversal(node.first)
        self.DFS_traversal(node.second)
        self.DFS_traversal(node.third)

    def inorder(self, node):
        
        if not node:
            return 

        if node.is_leaf():
            if node.keys[0]:
                print(node.keys[0])
            if node.keys[1]:
                print(node.keys[1])
        elif node.size == 1:
            self.inorder(node.first)
            if node.keys[0]:
                print(node.keys[0])
            if node.keys[1]:
                print(node.keys[1])
            self.inorder(node.second)
        elif node.size == 2:
            self.inorder(node.first)
            if node.keys[0]:
                print(node.keys[0])
            self.inorder(node.second)
            if node.keys[1]:
                print(node.keys[1])
            self.inorder(node.third)

def search(alist, item):
    i = bisect_left(alist, item)
    if i != len(alist) and alist[i] == item:
        return i

if __name__ == '__main__':
    root = None
    tree = B_2_3Tree()

    data = [i for i in range(1, 14)]
    for elem in data:
        root = tree.insert(root, elem)

    tree.DFS_traversal(root)