def diStringMatch(s: str) -> List[int]:
    increase_count = 0
    decrease_count = len(s)
    perm = []
    for letter in s:
        if letter == 'I':
            perm.append(increase_count)
            increase_count += 1
        elif letter == 'D':
            perm.append(decrease_count)
            decrease_count -= 1
    perm.append(increase_count)
    return perm