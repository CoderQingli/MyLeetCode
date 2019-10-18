def bitwiseComplement(self, N):
    """
    :type N: int
    :rtype: int
    """
    n = str(bin(N))[2:]
    n = n.replace("0", "2")
    n = n.replace("1", "0")
    n = n.replace("2", "1")
    return int(n, 2)