def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return None
    res = 0
    flag = False
    for i in range(len(s) - 1):
        if flag:
            flag = False
            continue
        if s[i] == "I":
            if s[i + 1] == "V":
                res += 4
                flag = True
            elif s[i + 1] == "X":
                res += 9
                flag = True
            else:
                res += 1
        if s[i] == "V":
            res += 5
        if s[i] == "X":
            if s[i + 1] == "L":
                res += 40
                flag = True
            elif s[i + 1] == "C":
                res += 90
                flag = True
            else:
                res += 10
        if s[i] == "L":
            res += 50
        if s[i] == "C":
            if s[i + 1] == "D":
                res += 400
                flag = True
            elif s[i + 1] == "M":
                res += 900
                flag = True
            else:
                res += 100
        if s[i] == "D":
            res += 500
        if s[i] == "M":
            res += 1000
    if flag:
        return res
    else:
        if s[-1] == "I":
            res += 1
        if s[-1] == "V":
            res += 5
        if s[-1] == "X":
            res += 10
        if s[-1] == "L":
            res += 50
        if s[-1] == "C":
            res += 100
        if s[-1] == "D":
            res += 500
        if s[-1] == "M":
            res += 1000
    return res