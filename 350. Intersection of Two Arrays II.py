def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    tmp = list(set(nums1) & set(nums2))
    res = []
    for i in tmp:
        times = min(nums1.count(i), nums2.count(i))
        res += [i] * times
    return res