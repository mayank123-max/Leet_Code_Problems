class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def addChild(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTree(data)
    def Inorder(self):
        element = []
        if self.left:
            element += self.left.Inorder()
        element.append(self.data)
        if self.right:
            element += self.right.Inorder()
        return element

def BuildTree(element):
    root = BinaryTree(element[0])
    for i in range(1,len(element)):
        root.addChild(element[i])
    return root

element = [1,2,3]
tree = BuildTree(element)
print(tree.Inorder())