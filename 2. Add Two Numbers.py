def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    res = ListNode(0)
    cur = res
    flag = 0
    while l1 or l2:
        if l1 and l2:
            flag, tmp = divmod(l1.val + l2.val + flag, 10)
        elif l1:
            flag, tmp = divmod(l1.val + flag, 10)
        else:
            flag, tmp = divmod(l2.val + flag, 10)
        cur.next = ListNode(tmp)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if flag == 1:
        cur.next = ListNode(flag)
    return res.next