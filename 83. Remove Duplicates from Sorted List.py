def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None
    res = head
    tmp = head
    while tmp.next != None:
        if tmp.next.val == tmp.val:
            tmp = tmp.next
        else:
            head.next = tmp.next
            head = head.next
            tmp = head
    head.next = None
    return res