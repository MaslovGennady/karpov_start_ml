def color_sort(nums):
    
    if nums is None or len(nums) == 0:
        return None
    
    if len(nums) == 1:
        return nums

    pos = 0
    
    for color in [0, 1]:
        
        end_color = 0
        start = pos 
            
        for idx in range(start, len(nums)):
            pos = idx
            if nums[idx] == color:
                continue
            else:
                for idx_inner in range(pos + 1, len(nums)):
                    if nums[idx_inner] == color:
                        # меняем idx элемент (правильный цвет) с pos элементом (неправильный цвет)
                        #print(f'color={color}', f'pos={pos}', nums)
                        nums[idx_inner], nums[pos] = nums[pos], nums[idx_inner]
                        #print(f'color={color}', f'pos={pos}', nums)
                        break
                    if nums[idx_inner] != color and idx_inner == len(nums) - 1:
                        end_color = 1
                        
            if end_color == 1:
                break
                        
            
    return nums     