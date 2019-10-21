def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if not s or len(set(s)) == 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[1]

    res = s[0]
    for i in range(len(s)):
        if len(res) >= len(s) - i:
            break
        for j in range(len(s), i, -1):
            if s[i:j] == s[i:j][::-1]:
                if j - i > len(res):
                    res = s[i:j]
    return res