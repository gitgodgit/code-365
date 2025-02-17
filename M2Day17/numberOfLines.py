def numberOfLines(widths: list[int], s: str) -> list[int]:
    total_length_inline = 0
    result = [1, 0]
    for letter in s:
        if total_length_inline + widths[ord(letter) - ord('a')] <= 100:
            total_length_inline += widths[ord(letter) - ord('a')]
        else:
            result[0] += 1
            total_length_inline = widths[ord(letter) - ord('a')]
    result[1] = total_length_inline
    return result



