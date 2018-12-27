def find_n_sum(nums, N, target, result, results):
    n = len(nums)

    if n < N or n < 2:
        return

    if N == 2:
        l, r = 0, n - 1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(n - N + 1):
            if target < nums[i] * N or target > nums[-1] * N:
                break
            if i == 0 or i > 0 and nums[i - 1] == nums[i]:
                find_n_sum(nums[i + 1:], N - 1, target - nums[i], result + [nums[i]], results)
    return

a = [1,0,-1,0,-2,2]
target = 0
results = []
a.sort()
find_n_sum(a, 4, target, [], results)
print results