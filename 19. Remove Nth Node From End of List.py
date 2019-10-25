def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    res = head
    tmp = head
    if not head:
        return
    while n > 0:
        tmp = tmp.next
        n -= 1
    if not tmp:
        return res.next
    while tmp:
        pre = head
        head = head.next
        tmp = tmp.next
    pre.next = pre.next.next
    return res