import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
Print all nodes in a linked list
"""
def printList(node):
    currNode = node
    while currNode:
        currData = currNode.data
        print("currData: %s" % currData)
        currNode = currNode.next

"""
Reverse a linked list
@:param headNode Node head node of current linked list
@:return headNode Node head node of reversed linked list
"""
def reverseList(headNode):
    if headNode == None:
        return None
    if headNode.next == None:
        return headNode

    currNode = headNode
    nextNode = headNode.next

    # unlink since headNode becomes tailNode and tailNode does not have next link
    headNode.next = None

    # loop until there is no nextNode
    while nextNode:
        # save next of NextNode into a tmp variable
        tmpNextNode = nextNode.next

        # change next link of nextNode
        nextNode.next = currNode

        # move pointers
        currNode = nextNode
        nextNode = tmpNextNode

    return currNode

"""
Main function
"""
def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node1.next.next = node3
    node1.next.next.next = node4
    node1.next.next.next.next = node5
    node1.next.next.next.next.next= node6
    node1.next.next.next.next.next.next = node7
    # printList(node1)

    reversedNode = reverseList(node1)
    printList(reversedNode)

if __name__ == "__main__":
    main()

