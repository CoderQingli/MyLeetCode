def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    tmp = []
    while head:
        tmp.append(head.val)
        head = head.next
    return tmp == tmp[::-1]