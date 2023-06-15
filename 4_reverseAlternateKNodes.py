class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseAlternateKNodes(head, k, reverseNextK=True):
    if head is None:
        return None

    prev = None
    curr = head

    if reverseNextK:
        count = 0
        while curr is not None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if curr is not None:
            head.next = reverseAlternateKNodes(curr, k, not reverseNextK)

        return prev
    else:
        count = 0
        while curr is not None and count < k:
            prev = curr
            curr = curr.next
            count += 1

        if curr is not None:
            prev.next = reverseAlternateKNodes(curr, k, not reverseNextK)

        return head



# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

# Reverse every alternate 3 nodes in the linked list
newHead = reverseAlternateKNodes(head, 3)

# Print the modified linked list: 3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 9 -> 8 -> 7
while newHead is not None:
    print(newHead.val, end=" ")
    newHead = newHead.next
