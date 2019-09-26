# 还可以用kmp算法来做

def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 0:
        return True
    for j in range(1, len(s)):
        tmp = s[:j]
        if len(s) % len(tmp) == 0:
            if tmp * (len(s) / len(tmp)) == s:
                return True
    return False