def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    for i in s:
        if i not in t:
            return False
        t = t[t.index(i) + 1:]
    return True