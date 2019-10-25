def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    tmp = ListNode(0)
    tmp.next = head
    res = tmp
    while tmp.next and tmp.next.next:
        a = tmp.next
        b = tmp.next.next
        tmp.next, b.next, a.next = b, a, b.next
        tmp = a
    return res.next