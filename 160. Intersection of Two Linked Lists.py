def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if not headA or not headB:
        return None
    if headA != headB and not headA.next and not headB.next:
        return None
    pa = headA
    while pa.next:
        pa = pa.next
    alast = pa
    pa.next = headB

    slow = headA
    fast = headA
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        alast.next = None
        return None

    currA = headA
    while (currA != fast):
        currA = currA.next
        fast = fast.next

    alast.next = None
    return currA