def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    res = ""
    tmp = 0
    while num1 or num2 or tmp != 0:
        if num1:
            tmp += (ord(num1[-1]) - ord("0"))
        if num2:
            tmp += (ord(num2[-1]) - ord("0"))
        res += str(tmp % 10)
        tmp = tmp // 10
        num1 = num1[:len(num1) - 1]
        num2 = num2[:len(num2) - 1]
    return res[::-1]

r = addStrings("1","1")
print(r)