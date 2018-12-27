def nextPermutation(nums):
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    
    if i <= 0:
        nums.sort()
        return
    
    j = len(nums) - 1
    while nums[j] <= nums[i - 1]:
        j -= 1
        
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
        
    return

nums = [1, 2, 3]
nextPermutation(nums)
print nums