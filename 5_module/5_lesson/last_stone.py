def last_stone(stones):
    import heapq
    # Создаем кучу из камней
    stones = [-stone for stone in stones]  # Используем отрицательные значения для макс-кучи
    heapq.heapify(stones)

    while len(stones) > 1:
        # Извлекаем два самых тяжелых камня
        x = -heapq.heappop(stones)
        y = -heapq.heappop(stones)

        # Если веса камней не равны, добавляем новый камень
        if x != y:
            heapq.heappush(stones, -abs(y - x))

    # Если остался один камень, возвращаем его вес, иначе возвращаем 0
    return -stones[0] if stones else 0