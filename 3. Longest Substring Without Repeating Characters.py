def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dic = {}
    res = i = j = 0
    while i < n and j < n:
        if s[j] not in dic:
            dic[s[j]] = 1
            j += 1
            res = max(res, j - i)
        else:
            del dic[s[i]]
            i += 1
    return res