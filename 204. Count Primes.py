def countPrimes(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return 0
    isprime = [True] * n
    isprime[0], isprime[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if isprime[i]:
            for j in range(i ** 2, n, i):
                isprime[j] = False
    res = 0
    for k in range(len(isprime)):
        if isprime[k]:
            res += 1
    return res