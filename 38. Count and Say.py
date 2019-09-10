def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    res = "1"
    for i in range(1, n):
        t = res[0]
        tmp = ""
        cnt = 0
        for j in range(len(res)):
            if res[j] == t:
                cnt += 1
            else:
                tmp = tmp + str(cnt) + t
                t = res[j]
                cnt = 1
            if j == len(res) - 1:
                tmp = tmp + str(cnt) + t
        res = tmp
    return res