def hasAlternatingBits(self, n):
    """
    :type n: int
    :rtype: bool
    """
    bits = bin(n)
    for i in range(2, len(bits) - 1):
        if bits[i] == bits[i + 1]:
            return False
    return True