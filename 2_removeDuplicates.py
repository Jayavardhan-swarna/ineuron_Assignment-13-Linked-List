class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    current = head
    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head



# Create the linked list: 11 -> 11 -> 11 -> 21 -> 43 -> 43 -> 60
head = ListNode(11)
head.next = ListNode(11)
head.next.next = ListNode(11)
head.next.next.next = ListNode(21)
head.next.next.next.next = ListNode(43)
head.next.next.next.next.next = ListNode(43)
head.next.next.next.next.next.next = ListNode(60)

# Remove duplicate nodes from the linked list
newHead = removeDuplicates(head)

# Print the modified linked list: 11 -> 21 -> 43 -> 60
while newHead is not None:
    print(newHead.val, end=" ")
    newHead = newHead.next
