def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            tmp1 = s[i:j]
            tmp2 = s[i + 1:j + 1]
            return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
    return True