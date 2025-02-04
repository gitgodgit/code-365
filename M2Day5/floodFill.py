def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    has_to_be_changed = image[sr][sc]
    if has_to_be_changed != color:
        image[sr][sc] = color
        if sr - 1 >= 0 and image[sr - 1][sc] == has_to_be_changed:
            floodFill(image, sr - 1, sc, color)
        if sr + 1 < len(image) and image[sr + 1][sc] == has_to_be_changed:
            floodFill(image, sr + 1, sc, color)
        if sc - 1 >= 0 and image[sr][sc - 1] == has_to_be_changed:
            floodFill(image, sr , sc - 1, color)
        if sc + 1 < len(image[sr]) and image[sr][sc + 1] == has_to_be_changed:
            floodFill(image, sr, sc + 1, color)
        return image
    else:
        return image



print(floodFill([[0,0,0],[0,1,0]], 0, 0, 2))
    