def backspaceCompare(self, S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """

    def helper(s):
        ans = []
        for c in s:
            if c != "#":
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)

    return helper(S) == helper(T)