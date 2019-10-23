def nsum(l, r, target, n, tmp):
    if n == 2:
        while l < r:
            if nums[l] + nums[r] == target:
                result.append(tmp + [nums[l]] + [nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(l, r + 1):
            if i == l or (i > l and nums[i] != nums[i - 1]):
                nsum(i + 1, r, target - nums[i], n - 1, tmp + [nums[i]])


nums.sort()
result = []
nsum(0, len(nums) - 1, target, 4, [])
return result