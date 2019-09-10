def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 and l2: return l2
    if not l2 and l1: return l1
    if not l1 and not l2: return None
    c1 = l1
    c2 = l2
    temp = ListNode(None)
    res = ListNode(None)
    res.next = temp
    while c1 and c2:
        if c1.val <= c2.val:
            temp.next = c1
            c1 = c1.next
            temp = temp.next
        else:
            temp.next = c2
            c2 = c2.next
            temp = temp.next
    temp.next = c1 or c2
    return res.next.next