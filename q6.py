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

    maxSingle = max(node.data, node.data + max(leftSum, rightSum))

    maxTop = max(maxSingle, node.data + leftSum + rightSum)

    findMaxSum.res = max(findMaxSum.res, maxTop)
    return maxSingle

"""
Find maximum path sum in a binary tree
@:param rootNode Node root node of binary tree
@:return maxSum int Integer containing sum of all of nodes data
"""
def findMaxSum(rootNode):
    findMaxSum.res = float("-inf")
    __findMaxSumNode(rootNode)
    return findMaxSum.res

"""
Main function
"""
def main():

    # First tree
    # root = Node(10)
    # root.left = Node(2)
    # root.right = Node(10)
    # root.left.left = Node(20)
    # root.left.right = Node(1)
    # root.right.right = Node(-25)
    # root.right.right.left = Node(3)
    # root.right.right.right = Node(4)

    # Second tree
    root = Node(-15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)
    maxSum = findMaxSum(root)
    print("maxSum: %s" % maxSum)

if __name__ == "__main__":
    main()

