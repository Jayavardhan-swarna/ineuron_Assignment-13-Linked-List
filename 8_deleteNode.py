class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def deleteNode(head, position):
    # If the list is empty, return the list as it is
    if head is None:
        return head

    # Case 1: Delete the head node
    if position == 1:
        new_head = head.next
        if new_head is not None:
            new_head.prev = None
        return new_head

    current = head
    count = 1

    # Traverse to the node at the given position
    while current is not None and count < position:
        current = current.next
        count += 1

    # If the node to be deleted is the last node
    if current.next is None:
        current.prev.next = None
    else:
        # Update the next and prev pointers of adjacent nodes
        current.prev.next = current.next
        current.next.prev = current.prev

    return head


# Create the doubly linked list: 1 <--> 5 <--> 2 <--> 9
head = Node(1)
head.next = Node(5)
head.next.prev = head
head.next.next = Node(2)
head.next.next.prev = head.next
head.next.next.next = Node(9)
head.next.next.next.prev = head.next.next

# Delete the node at position 1
head = deleteNode(head, 1)

# Print the updated doubly linked list: 5 <--> 2 <--> 9
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
