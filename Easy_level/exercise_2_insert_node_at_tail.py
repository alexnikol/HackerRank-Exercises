"""This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.
You are given the pointer to the head node of a linked list and an integer to add to the list.
Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of
the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list
is empty.
-- Input Format
You have to complete the SinglyLinkedListNode insertAtTail(SinglyLinkedListNode head, int data) method.
It takes two arguments: the head of the linked list and the integer to insert at tail. You should not read any input from the stdin/console.
The input is handled by code editor and is as follows:
The first line contains an integer , denoting the elements of the linked list.
The next  lines contain an integer each, denoting the element that needs to be inserted at tail.
"""

from Helpers.linked_list import SinglyLinkedListNode


def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    else:
        current_node = head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = SinglyLinkedListNode(data)
        return head


# RESULT

node1 = SinglyLinkedListNode(1)
node2 = SinglyLinkedListNode(2)
node3 = SinglyLinkedListNode(3)
node1.next = node2
node2.next = node3

result = insertNodeAtTail(node1, 34)

current_node = result

while current_node is not None:
    print(current_node.data)
    current_node = current_node.next