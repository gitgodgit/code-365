def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    counter = 0
    i = 1
    if flowerbed[0] == 0:
        if len(flowerbed) < 2 or flowerbed[1] != 1:
            counter += 1
            flowerbed[0] = 1
            if len(flowerbed) > 1:
                flowerbed[1] = 2
    while i < len(flowerbed) -1:
        if flowerbed[i] == 0:
            if flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                counter += 1 
                flowerbed[i - 1], flowerbed[i], flowerbed[i + 1] = 2, 1, 2
        i+= 1
    if flowerbed[-1] == 0:
        if len(flowerbed) < 2 or flowerbed[-2] != 1:
            counter += 1
            flowerbed[-1] = 1
            if len(flowerbed) > 1:
                flowerbed[-2] = 2
    
    return counter >= n
