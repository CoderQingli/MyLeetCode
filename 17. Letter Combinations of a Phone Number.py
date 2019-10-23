def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def helper(tmp, d):
        if len(d) == 0:
            res.append(tmp)
        else:
            for i in phone[d[0]]:
                helper(tmp + i, d[1:])

    res = []
    if digits:
        helper("", digits)
    return res