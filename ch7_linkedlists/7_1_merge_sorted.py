class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False
    def __str__(self):
        current = self
        arr = []
        while current:
            arr.append(current.data)
            current = current.next
        return " ".join([str(i) for i in arr])

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

dummy1 = l1 = ListNode(0)
dummy2 = l2 = ListNode(0)
for i in arr1:
    l1.next = ListNode(i)
    l1 = l1.next
for i in arr2:
    l2.next = ListNode(i)
    l2 = l2.next
l1 = dummy1.next
l2 = dummy2.next
print(merge_two(l1,l2))