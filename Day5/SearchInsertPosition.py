class SearchInserposition:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        if target > max(nums):
            return len(nums) - 1
        