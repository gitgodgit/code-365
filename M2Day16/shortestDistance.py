def shortestToChar(s: str, c: str) -> list[int]:
    distances = []
    distance_forward = -1
    distance_backward = -1
    for i in range(len(s)):
        for k in range(i,len(s)):
            if s[k] == c:
                distance_forward = k - i
                break
        for j in range(i, -1, -1):
            if s[j] == c:
                distance_backward = i - j
                break
        
        if distance_forward == -1 and distance_backward != -1:
            distance_forward = distance_backward
        elif distance_forward != -1 and distance_backward == -1:
            distance_backward = distance_forward
            
        distances.append(min(distance_forward, distance_backward))
        distance_backward = -1
        distance_forward = -1
    return distances
        