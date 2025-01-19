def longestCommonPrefix(strs:list[str]) -> str:
    prefix = "" 
    for i in range(len(strs[0])):
        checking_letter = strs[0][i]
        for j in range(len(strs)):
            if len(strs[j]) < i + 1 or strs[j][i] != checking_letter:
                return prefix
            elif strs[j][i] == strs[0][i] and j == len(strs) - 1:
                prefix = prefix + strs[0][i]
    return prefix