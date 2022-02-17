from linked_list import LinkedList
from list_node import ListNode
def merge_two(l1, l2):
    dummy = head = ListNode(0)
    while l1 and l2:
        if (l1.data < l2.data):
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    if not l1:
        l1 = l2
    head.next = l1
    return dummy.next


arr1 = [1,3,5,7,9]
arr2 = [2,4,6,8,10]

l1 = LinkedList(0)
l2 = LinkedList(0)
l1.create_from_list(arr1)
l2.create_from_list(arr2)
print(l1,l2)
print(merge_two(l1.head,l2.head))