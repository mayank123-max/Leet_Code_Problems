class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def buildTree(inOrder, preOrder, inStrt, inEnd):
	
	if (inStrt > inEnd):
		return None
	tNode = Node(preOrder[buildTree.preIndex])
	buildTree.preIndex += 1

	if inStrt == inEnd :
		return tNode

	inIndex = search(inOrder, inStrt, inEnd, tNode.data)
	
	tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
	tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

	return tNode

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i

def postorder(root,l=[]):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    l.append(root.data)
	
inp1 = list(map(int,input().split()))
inp2 = list(map(int,input().split()))

buildTree.preIndex = 0
root = buildTree(inp1, inp2, 0, len(inp1)-1)
print(postorder(root))