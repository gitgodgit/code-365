def removeElement(nums: list[int], val: int) -> int:
    counter = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != val:
            counter += 1
        else:
            for j in range(i, len(nums) - 1):
                nums[j] = nums[j+1]
                
    return counter

def removeElementTwoPointers(nums, val):
    write_pointer = 0

    for readpointer in range(len(nums)):
        if nums[readpointer] != val:
            nums[write_pointer] = nums[readpointer]
            write_pointer += 1

    return write_pointer

