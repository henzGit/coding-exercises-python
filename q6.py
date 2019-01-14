"""
Node for Binary Tree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
Find maximum path sum for a leaf node in binary tree
@:param node Node node from which we want to calculate the max path sum
@:return maxSum int Integer whose value represents the max path sum from the given node
"""
def __findMaxSumNode(node):
    if node == None:
        return 0
    leftSum = __findMaxSumNode(node.left)
    rightSum = __findMaxSumNode(node.right)

    maxSum = max(
        node.data,
        node.data + leftSum,
        node.data + rightSum
    )

    return maxSum

"""
Find maximum path sum in a binary tree
@:param rootNode Node root node of binary tree
@:return maxSum int Integer containing sum of all of nodes data
"""
def findMaxSum(rootNode):
    leftSum = __findMaxSumNode(rootNode.left)
    print("leftSum: %s" %leftSum)
    rightSum = __findMaxSumNode(rootNode.right)
    print("rightSum: %s" %rightSum)

    maxSum = max(
        rootNode.data,
        rootNode.data + leftSum,
        rootNode.data + rightSum,
        rootNode.data + leftSum + rightSum
    )

    return maxSum

"""
Main function
"""
def main():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    maxSum = findMaxSum(root)
    print("maxSum: %s" % maxSum)

if __name__ == "__main__":
    main()

