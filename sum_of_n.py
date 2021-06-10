def sum_of_n(n):
    # return sum of first n integers.
    res = 0 
    for i in range(1 , n+1):
        res += i
        i+=1
    
    return res


results = sum_of_n(5)
print(results)