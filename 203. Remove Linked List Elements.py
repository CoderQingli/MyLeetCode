def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if not head:
        return None
    while head and head.val == val:
        head = head.next
    if not head:
        return None
    res = head
    tmp = head
    head = head.next
    while head:
        if head.val == val:
            tmp.next = head.next
            head = head.next
        else:
            tmp = head
            head = head.next
    return res