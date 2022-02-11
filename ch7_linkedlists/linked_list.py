from list_node import ListNode
class LinkedList:
    head = None
    def __init__(self, val=0):
        self.head = ListNode(val)
    def create_from_list(self, L):
        self.head = ListNode(L[0])
        current = self.head
        for val in L[1:]:
            current.next = ListNode(val)
            current = current.next
    def append(self, val):
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        return current.next

    def search(self, val):
        cur = self.head
        while cur:
            if cur.data == val:
                return cur
        return None

    def __str__(self):
        cur = self.head
        ans = []
        while cur:
            ans.append(cur.data)
            cur = cur.next
        return str(ans)
