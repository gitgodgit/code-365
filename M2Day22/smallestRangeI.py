def smallestRangeI(nums: list[int], k: int) -> int:
    maximum = max(nums)
    minimum = min(nums)
    average = round((maximum + minimum) / 2)
    if maximum - minimum >= 2 * k:
        for i in range(len(nums)):
            if nums[i] == maximum:
                nums[i] -= k
            elif nums[i] == minimum:
                nums[i] += k
            elif nums[i] < average:
                nums[i] += min(average - nums[i], k)
            elif nums[i] > average:
                nums[i] -= min(nums[i] - average, k)
    else:
        for i in range(len(nums)):
            if nums[i] == maximum:
                nums[i] -= maximum - average
            elif nums[i] == minimum:
                nums[i] += average - minimum
            elif nums[i] < average:
                nums[i] += min(average - nums[i], k)
            elif nums[i] > average:
                nums[i] -= min(nums[i] - average, k)
    
    return max(nums) - min(nums)

def optimisedSmallestRangeI(nums: l[int], k: int) -> int:
        maximum = max(nums)
        minimum = min(nums)
        average = round((maximum + minimum) / 2)
        for i in range(len(nums)):
            if nums[i] < average:
                nums[i] += min(average - nums[i], k)
            elif nums[i] > average:
                nums[i] -= min(nums[i] - average, k)
        return max(nums) - min(nums)

def oneLinerSmallestRangeI(nums: l[int], k: int) -> int:
    return max(0, max(nums) - min(nums) - 2 * k)
