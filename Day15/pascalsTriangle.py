def generate(numRows)->list[list(int)]:
    list_of_lists = []
    for i in range(numRows):
        new_list = [1]
        for j in range(i+1):
            if j == 0:
                continue
            if j == i:
                new_list.append(1)
            else:
                new_list.append(list_of_lists[i-1][j-1] + list_of_lists[i-1][j])
        list_of_lists.append(new_list)
    return list_of_lists
