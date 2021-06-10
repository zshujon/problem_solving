def longest_common_prefix(arr):    
    arr_len = len(arr)
 
    if (arr_len == 0):
        return ""
    if (arr_len == 1):
        return arr[0]
 
    arr.sort()    
    min_str_len = min(len(arr[0]), len(arr[-1]))
 
    i = 0
    while (i < min_str_len and arr[0][i] == arr[-1][i]):
        i += 1
 
    pre = arr[0][0: i]

    return pre
 
if __name__ == "__main__":
    arrs = [["commnication", "competition", "complain", "complete"],
            ['copy', 'adult', 'facebook', 'amazon']]
    
    for arr in arrs: 
        print("The longest Common Prefix is :" , longest_common_prefix(arr))
 