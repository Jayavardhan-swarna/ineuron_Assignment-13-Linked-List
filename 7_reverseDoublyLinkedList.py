class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def reverseDoublyLinkedList(head):
    current = head
    prev = None

    while current is not None:
        # Swap the next and prev pointers of the current node
        current.next, current.prev = current.prev, current.next

        # Move to the next node
        prev = current
        current = current.prev

    # Update the head pointer to the last node visited
    head = prev

    return head


# Create the original doubly linked list: 10 -> 8 -> 4 -> 2
head = Node(10)
head.next = Node(8)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next
head.next.next.next = Node(2)
head.next.next.next.prev = head.next.next

# Reverse the doubly linked list
head = reverseDoublyLinkedList(head)

# Print the reversed doubly linked list: 2 -> 4 -> 8 -> 10
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
