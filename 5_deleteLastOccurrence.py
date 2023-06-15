class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteLastOccurrence(head, key):
    if head is None:
        return None

    prev = None
    curr = head
    count = 0

    # Find the last occurrence of the key and update prev and curr
    while curr is not None:
        if curr.val == key:
            prev = curr
            count += 1
        curr = curr.next

    # Delete the last occurrence if found
    if prev is not None:
        prev.next = prev.next.next
        count -= 1

    # Check if the key was the last occurrence
    if count == 0:
        return head
    else:
        return prev


# Create the linked list: 1 -> 2 -> 3 -> 5 -> 2 -> 10
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(10)

# Delete the last occurrence of key = 2
newHead = deleteLastOccurrence(head, 2)

# Print the modified linked list: 1 -> 2 -> 3 -> 5 -> 10
while newHead is not None:
    print(newHead.val, end=" ")
    newHead = newHead.next
