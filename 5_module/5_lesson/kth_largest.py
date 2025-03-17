def kth_largest(array, k):
    
    if array is None or len(array) == 0:
        return None
    
    import random
    
    def quickselect(array, k):
    
        if len(array) == 1:
            return - array[0]
    
        # Выбираем случайный опорный элемент
        pivot_index = random.randint(0, len(array) - 1)
        pivot = array[pivot_index]
    
        # Разделяем массив на три части
        left = [x for i, x in enumerate(array) if x < pivot and i != pivot_index]
        middle = [x for x in array if x == pivot]
        right = [x for i, x in enumerate(array) if x > pivot and i != pivot_index]
    
        # Рекурсивно ищем k-й наименьший элемент
        if k <= len(left):
            return quickselect(left, k)
        elif k <= len(left) + len(middle):
            return - middle[0]
        else:
            return quickselect(right, k - len(left) - len(middle))

    # Преобразуем задачу в поиск k-го наименьшего элемента в массиве, перевернутом по значению
    return quickselect([-x for x in array], k)

