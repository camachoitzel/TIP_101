def contains_duplicates(nums):
    # sort the list
    nums.sort()

    for num in range(1 ,len(nums)):
        if nums[num] == nums[num - 1]:
            return True
        return False
    
def frequency_greater_than_n(nums, n):
    nums.sort()
    count = 1
    result= {}

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1

        else:
            if count > n:
                result[nums[i - 1]] = count
            count = 1

    if len(nums) > 0 and count > n:
        result[nums[-1]] = count
    
    return result
    
        