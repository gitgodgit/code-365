def singleNumber(nums: list[int]) -> int:
    my_dict = {}
    for integer in nums:
        if integer not in my_dict:
            my_dict[integer] = 1
        else:
            my_dict[integer] += 1
    
    for item in my_dict:
        if my_dict[item] == 1:
            return item


def singleNumberBitwise(nums: list[int]) -> int:
        answer = 0
        for number in nums:
            answer ^= number
        return answer
