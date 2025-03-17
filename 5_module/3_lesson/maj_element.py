def maj_element(nums):
    if nums is None or len(nums) == 0:
        return None
    counter = {}
    maj_cnt = len(nums) // 2 if len(nums) > 1 else 1
    for elem in nums:
        new_cnt = counter.get(elem, 0) + 1
        counter[elem] = new_cnt
        if new_cnt == maj_cnt:
            return elem