def countCharacters(self, words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    res = 0
    for w in words:
        f = 0
        tmp = list(chars)
        for i in w:
            if i in tmp:
                tmp.remove(i)
            else:
                f = 1
                break
        if f == 0:
            res += len(w)
    return res