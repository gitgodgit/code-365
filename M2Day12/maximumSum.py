def maximumSum(nums: list[int]) -> int:
    storage_digits_sum = {}
    max_sum = -1
    for num in nums:
        digits_sum = sum(int(d) for d in str(abs(num)))
        storage_digits_sum.setdefault(digits_sum, []).append(num)

    for key,value in storage_digits_sum.items():
        if len(value) > 1:
            sorted_value = sorted(value, reverse = True)
            sum_of_high = sorted_value[0] + sorted_value[1]
            max_sum = max(max_sum, sum_of_high)
    return max_sum


