def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    tmp = int("0b" + "1" * (len(bin(num)) - 2), 2)
    return num ^ tmp