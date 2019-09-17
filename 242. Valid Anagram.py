def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    cnts = {}
    cntt = {}
    for i in range(len(s)):
        if s[i] in cnts:
            cnts[s[i]] += 1
        else:
            cnts[s[i]] = 1
        if t[i] in cntt:
            cntt[t[i]] += 1
        else:
            cntt[t[i]] = 1
    return cnts == cntt