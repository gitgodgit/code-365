def distributeCandies(candyType: list[int]) -> int:
    halved_candy = []
    copy_candyType = candyType
    full_size = len(copy_candyType)
    counter = 0
    for i in range(len(copy_candyType) - counter):
        if copy_candyType[i] not in halved_candy:
            halved_candy.append(copy_candyType[i])
            copy_candyType.remove(copy_candyType[i])
            counter += 1
        if len(halved_candy) == full_size / 2:
            break
    for i in range(len(copy_candyType)):
        if len(halved_candy) < full_size // 2:
            halved_candy.append(copy_candyType[i])
        else:
            break
    return len(halved_candy)
        
        