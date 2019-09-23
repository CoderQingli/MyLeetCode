def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in range(len(s)):
        if dic[s[i]] == 1:
            return i
    return -1