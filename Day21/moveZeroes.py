def moveZeroes(nums:list) -> list:
    count = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            count += 1
            for j in range(i, len(nums) - 1):
                nums[j] = nums[j + 1]
    start_index = len(nums) - count
    for k in range(start_index, len(nums) ):
        nums[k] = 0

def swapZeroes(nums:list) -> list:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
