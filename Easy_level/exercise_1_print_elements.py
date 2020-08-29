"""
Given a pointer to the head node of a linked list, print its elements in order, one element per line.
If the head pointer is null (indicating the list is empty), don’t print anything.
-- Input Format
The first line of input contains n, the number of elements in the linked list.
The next n lines contain one element each, which are the elements of the linked list.
Note: Do not read any input from stdin/console. Complete the printLinkedList function in the editor below.
"""

from Helpers.linked_list import SinglyLinkedListNode


def printLinkedList(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.data)
        currentNode = currentNode.next


# RESULT

node1 = SinglyLinkedListNode(1)
node2 = SinglyLinkedListNode(2)
node3 = SinglyLinkedListNode(3)
node1.next = node2
node2.next = node3

printLinkedList(node1)

