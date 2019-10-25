def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []

    def helper(s, l, r):
        if len(s) == 2 * n:
            res.append(s)
            return
        if l < n:
            helper(s + '(', l + 1, r)
        if r < l:
            helper(s + ')', l, r + 1)

    helper('', 0, 0)
    return res