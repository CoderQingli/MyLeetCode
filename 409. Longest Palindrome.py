def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: int
    """
    dic = {}
    res = 0
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for c in dic:
        res += dic[c] // 2
    res *= 2
    if res == len(s):
        return res
    else:
        return res + 1