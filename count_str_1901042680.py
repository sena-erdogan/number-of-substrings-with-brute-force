def count_str(str, start, end):
    count = 0
    
    for i in range(0, len(str)):
        if str[i] == start:
            for j in range(i, len(str)):
                if str[j] == end:
                    count += 1
    print("Count: ", count)
    
    return;
    
count_str("TXZXXJZW", 'X', 'Z')
