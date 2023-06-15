class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createNewList(list1, list2):
    dummy = ListNode()  # Dummy node as the head of the new list
    newList = dummy  # Pointer to the current node in the new list

    ptr1 = list1  # Pointer to traverse list1
    ptr2 = list2  # Pointer to traverse list2

    while ptr1 is not None and ptr2 is not None:
        if ptr1.val >= ptr2.val:
            newList.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
        else:
            newList.next = ListNode(ptr2.val)
            ptr2 = ptr2.next
        newList = newList.next

    # Append the remaining nodes of list1 or list2, if any
    while ptr1 is not None:
        newList.next = ListNode(ptr1.val)
        ptr1 = ptr1.next
        newList = newList.next

    while ptr2 is not None:
        newList.next = ListNode(ptr2.val)
        ptr2 = ptr2.next
        newList = newList.next

    return dummy.next  # Return the new list without the dummy node


# Create list1: 5 -> 2 -> 3 -> 8
list1 = ListNode(5)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(8)

# Create list2: 1 -> 7 -> 4 -> 5
list2 = ListNode(1)
list2.next = ListNode(7)
list2.next.next = ListNode(4)
list2.next.next.next = ListNode(5)

# Create the new list using list1 and list2
newList = createNewList(list1, list2)

# Print the values of the new list
while newList is not None:
    print(newList.val, end=" ")
    newList = newList.next
