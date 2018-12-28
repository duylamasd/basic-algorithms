def maxSubArray(nums):
    n = len(nums)
    mFar = nums[0]
    curr = nums[0]

    if n < 2:
        return curr

    for i in range(1, n):
        curr = max(nums[i], curr + nums[i])
        mFar = max(mFar, curr)

    return mFar
