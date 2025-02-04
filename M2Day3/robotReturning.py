def judgeCircle(moves: str) -> bool:
    count_U = 0
    count_D = 0
    count_L = 0
    count_R = 0
    for i in range(len(moves)):
        if moves[i] == 'U':
            count_U += 1
        elif moves[i] == 'D':
            count_D += 1
        elif moves[i] == 'L':
            count_L += 1
        elif moves[i] == 'R':
            count_R += 1
    
    return count_D == count_U and count_R == count_L


def judgeCircleSolution(self, moves: str) -> bool:
    return (moves.count('R') == moves.count('L'))  & (moves.count('U') == moves.count('D'))