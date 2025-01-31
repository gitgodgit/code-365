def constructRectangle(area: int) ->list[int]:
    for W in range(int(sqrt(area)), -1 , -1):
        if area % W == 0:
            L = area // W 
            return [L, W]