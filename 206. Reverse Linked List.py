def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None
    if not head.next:
        return head
    cur = head.next
    head.next = None
    while cur.next:
        tmp = cur.next
        cur.next = head
        head = cur
        cur = tmp
    cur.next = head
    return cur