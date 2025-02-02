def distributeCandies(candyType: list[int]) -> int:
    halved_candy = set()
    copy_candyType = candyType
    full_size = len(copy_candyType)
    for i in range(full_size):
        if copy_candyType[i]:
            halved_candy.add(copy_candyType[i])
        if len(halved_candy) == full_size / 2:
            break
    return len(halved_candy)

def distributeCandies2(candyType: list[int]):
    unique_candies = set(candyType)
    return min(len(unique_candies), len(candyType) // 2)
        
        