def toHex(self, num):
    """
    :type num: int
    :rtype: str
    """
    res = ""
    if num == 0: return "0"
    if num < 0: num = 0xffffffff + 1 + num
    while num:
        num, tmp = divmod(num, 16)
        res += str(tmp if tmp < 10 else unichr(ord('a') + (tmp % 10)))

    return res[::-1]