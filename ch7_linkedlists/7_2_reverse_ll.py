from linked_list import LinkedList
from list_node import ListNode
def reverse_list(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    while head:
        temp = dummy.next
        dummy.next = head
        head = head.next
        dummy.next.next = temp
    return dummy.next

head = LinkedList(5)
head.create_from_list([1,2,3])
print(reverse_list(head.head))