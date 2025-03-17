def merge_sort(arr):
    #print(f'merge_sort in={arr}')
    if arr is None or len(arr) == 0:
        return arr
    
    def merge(a, b):
        #print(f'merge in a={a}, b={b}')
        # merges two sorted arrays
        
        if a is None or len(a) == 0:
            return b
        if b is None or len(b) == 0:
            return a
        
        res = []
        a_ind = 0
        b_ind = 0
        
        while a_ind < len(a):
            if b_ind >= len(b) or a[a_ind] <= b[b_ind]:
                res.append(a[a_ind])
                a_ind += 1
            else:
                res.append(b[b_ind])
                b_ind += 1
        
        if b_ind < len(b):
            for i in range(b_ind, len(b)):
                res.append(b[i])
          
        #print(f'merge out res={res}')
        return res
    
    if len(arr) > 1:
        arr = merge(merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:]))
    else:
        return arr
        #print(f'merge_sort out={arr}')
        
    #print(f'merge_sort out={arr}')
    return arr 