def small (nums):
    result = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                result[i] += 1
    return result
nums=[8,1,2,2,3]
print("nums=",nums)
print("output=",small(nums))
