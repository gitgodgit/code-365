def findShortestSubArray(nums: list[int]) -> int:
    frequency = {}
    start_index = {}
    finish_index = {}
    for i in range(len(nums)):
        if nums[i] in frequency:
            frequency[nums[i]] += 1
            finish_index[nums[i]] = i
        else:
            frequency[nums[i]] = 1
            start_index[nums[i]] = i
            finish_index[nums[i]] = i   
    
    max_repeated_key = max(frequency, key = frequency.get)
    max_repeated_value = frequency[max_repeated_key]
    minimal_length = finish_index[max_repeated_key] - start_index[max_repeated_key]

    for key, value in frequency.items():
        if value == max_repeated_value:
            length = finish_index[key] - start_index[key]
            if length < minimal_length:
                minimal_length = length
    return minimal_length + 1