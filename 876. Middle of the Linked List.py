def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    s = head
    f = head
    while f and f.next:
        f = f.next.next
        s = s.next
    return s