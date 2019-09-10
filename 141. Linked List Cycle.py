def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head or not head.next:
        return False
    fast = head.next
    slow = head
    while fast != slow:
        if not fast or not fast.next:
            return False
        fast = fast.next.next
        slow = slow.next
    return True