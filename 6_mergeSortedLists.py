class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeSortedLists(a, b):
    dummy = ListNode()  # Dummy node as the head of the merged list
    curr = dummy

    # Compare the values of nodes from both linked lists
    while a is not None and b is not None:
        if a.val <= b.val:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next

    # Append the remaining nodes of the non-empty linked list
    if a is not None:
        curr.next = a
    else:
        curr.next = b

    return dummy.next  # Return the head of the merged list


# Create the first linked list: 5 -> 10 -> 15
a = ListNode(5)
a.next = ListNode(10)
a.next.next = ListNode(15)

# Create the second linked list: 2 -> 3 -> 20
b = ListNode(2)
b.next = ListNode(3)
b.next.next = ListNode(20)

# Merge the two sorted linked lists
mergedHead = mergeSortedLists(a, b)

# Print the merged linked list: 2 -> 3 -> 5 -> 10 -> 15 -> 20
while mergedHead is not None:
    print(mergedHead.val, end=" ")
    mergedHead = mergedHead.next
