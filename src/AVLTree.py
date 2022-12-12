class AVLNode():

    def __init__(self, value):
        
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree():
    
    def calculate_height(self, node):

        if not node:
            return 0

        return node.height

    def calculate_bf(self, node):
        
        return self.calculate_height(node.left) - self.calculate_height(node.right)

    def update_height(self, node):

        hl = self.calculate_height(node.left)
        hr = self.calculate_height(node.right)
        
        if hl > hr:
            node.height = hl + 1
        else:
            node.height = hr + 1

    def right_rotation(self, node):
        
        q = node.left
        node.left = q.right
        q.right = node
        
        self.update_height(node)
        self.update_height(q)

        return q

    def left_rotation(self, node):

        q = node.right
        node.right = q.left
        q.left = node

        self.update_height(node)
        self.update_height(q)

        return q

    def previous(self, node, root = None):

        if root:
            current = root
            predeccesor = None

            while current:
                if current.value < node.value:
                    predeccesor = current
                    current = current.right
                else:
                    current = current.left

            return predeccesor            
        else:
            if not node:
                return None

            tmp_node = node.left
            
            if tmp_node:
                while tmp_node.right:
                    tmp_node = tmp_node.right
                
            return tmp_node

    def next(self, root, node):

        current = root
        succesor = None

        while current:
            if current.value > node.value:
                succesor = current
                current = current.left
            else:
                current = current.right

        return succesor

    def insert(self, node, value):
        
        if not node:
            return AVLNode(value)
        if node.value == value:
            return node
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        self.update_height(node)

        bf = self.calculate_bf(node)

        return self.balance(node, bf)

    def delete(self, node, value):

        if not node:
            return node
        if value > node.value:
            node.right = self.delete(node.right, value)
        elif value < node.value:
            node.left = self.delete(node.left, value)
        else:
            if not node.left:
                tmp_node = node.right
                node = None

                return tmp_node
            
            elif not node.right:
                tmp_node = node.left
                node = None

                return tmp_node

            else:
                tmp_node = self.previous(node)
                node.value = tmp_node.value
                node.left = self.delete(node.left, tmp_node.value)
        
        self.update_height(node)

        bf = self.calculate_bf(node)

        return self.balance(node, bf)

    def search(self, node, value):

        if not node or node.value == value:
            return node
        if node.value < value:
            return self.search(node.right, value)
        else:
            return self.search(node.left, value)

    def DFS_traversal(self, node):

        if not node:
            return
        
        print(f"{node.value} ", end="") 
        self.DFS_traversal(node.left)
        self.DFS_traversal(node.right)

    def balance(self, node, bf):
        if bf < -1 and self.calculate_bf(node.right) == -1:
            return self.left_rotation(node)

        elif bf < -1 and self.calculate_bf(node.right) == 1:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)

        elif bf > 1 and self.calculate_bf(node.left) == -1:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)

        elif bf > 1 and self.calculate_bf(node.left) == 1:
            return self.right_rotation(node)

        return node

# myTree = AVLTree()
# root = None
 
# root = myTree.insert(root, 10)
# root = myTree.insert(root, 20)
# #root = myTree.insert(root, 30)

# root = myTree.delete(root, 10)

# root = myTree.insert(root, 30)

# myTree.DFS_traversal(root)