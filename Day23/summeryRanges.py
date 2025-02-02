def summeryRanges(nums: list[int]) -> list[str]:
    if not nums:
        return []
    start = nums[0]
    ranges = []
    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i + 1] != nums[i] + 1:
            finish = nums[i]
            if start == finish:
                ranges.append(f"{finish}")
            else:
                ranges.append(f"{start}->{finish}")
            if i != len(nums) - 1:
                start = nums[i + 1]
    return ranges