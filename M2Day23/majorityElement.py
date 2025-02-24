def majorityElement(nums: list[int]) -> int:
    if len(nums) % 2 == 0:
        majority_number = len(nums) // 2
    else:
        majority_number = len(nums) // 2 + 1
    nums_set = set(nums)
    for each in nums_set:
        if nums.count(each) >= majority_number:
            return each

def mahorityElementSorting(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]