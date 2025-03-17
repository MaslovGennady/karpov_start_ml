def kth_smallest(root, k):
    stack = []
    current = root
    count = 0

    while True:
        # Идем в самый левый узел
        while current:
            stack.append(current)
            current = current.left

        # Если стек пуст, значит, мы обошли все элементы
        if not stack:
            break

        # Извлекаем верхний элемент из стека
        node = stack.pop()
        count += 1

        # Если это k-ый элемент, возвращаем его значение
        if count == k:
            return node.val

        # Переходим к правому поддереву
        current = node.right

    # Если k больше количества элементов в дереве
    return None