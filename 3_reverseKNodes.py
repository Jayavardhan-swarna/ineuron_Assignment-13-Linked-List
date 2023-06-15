class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseSegment(head, k):
    prev = None
    curr = head
    for _ in range(k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def reverseKNodes(head, k):
    if head is None or k == 1:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head
    count = 0

    while curr is not None:
        count += 1
        if count % k == 0:
            prev = reverseSegment(prev, curr.next)
            curr = prev.next
        else:
            curr = curr.next

    return dummy.next


# Create the linked list: 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

# Reverse every 4 nodes in the linked list
newHead = reverseKNodes(head, 4)

# Print the modified linked list: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5
while newHead is not None:
    print(newHead.val, end=" ")
    newHead = newHead.next
