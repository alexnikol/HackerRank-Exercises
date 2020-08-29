"""
You’re given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer, insert this node at the head of the linked list and return the new head node. The head pointer given may be null meaning that the initial list is empty.
Input Format
You have to complete the SinglyLinkedListNode Insert(SinglyLinkedListNode head, int data) method which takes two arguments - the head of the linked list and the integer to insert. You should NOT read any input from stdin/console.
The input is handled by code in the editor and is as follows:
The first line contains an integer n, denoting the number of elements to be inserted at the head of the list.
The next n lines contain an integer each, denoting the element to be inserted.
"""

from Helpers.linked_list import SinglyLinkedListNode

def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    node.next = llist
    return node


# RESULT

node1 = SinglyLinkedListNode(1)
node2 = SinglyLinkedListNode(2)
node3 = SinglyLinkedListNode(3)
node1.next = node2
node2.next = node3

result = insertNodeAtHead(node1, 33)
current_node = result

while current_node is not None:
    print(current_node.data)
    current_node = current_node.next