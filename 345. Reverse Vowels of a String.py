def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    l = 0
    r = len(s) - 1
    s = list(s)
    v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    while l < r:
        while s[l] not in v and l < r:
            l += 1
        while s[r] not in v and l < r:
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    s = "".join(s)
    return s