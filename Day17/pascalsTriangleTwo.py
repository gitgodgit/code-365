def getRow(rowIndex: int) -> list[int]:
    row = [1]
    count = 0
    while count < rowIndex:
        new_row = [1]
        for i  in range(1, count + 1):
            new_row.append(row[i-1] + row[i])
        new_row.append(1)
        row = new_row
        count+=1 
    return row
    
        