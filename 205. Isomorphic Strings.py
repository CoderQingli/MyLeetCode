def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    check = {}
    check2 = {}
    for i in range(len(s)):
        if s[i] not in check:
            if t[i] in check2:
                return False
            check[s[i]] = t[i]
            check2[t[i]] = s[i]
        elif check[s[i]] != t[i]:
            return False
    return True