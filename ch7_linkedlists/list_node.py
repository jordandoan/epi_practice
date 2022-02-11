class ListNode:
    data = 0
    next = None

    def __init__(self, val=0,next=None):
        self.data = val
        self.next = next

    def __str__(self):
        current = self
        ans = []
        while current:
            ans.append(current.data)
            current = current.next
        return str(ans)
