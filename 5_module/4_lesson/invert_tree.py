def invert_tree(head):
    if head is not None:
        head.left, head.right = head.right, head.left
        head.left = invert_tree(head.left)
        head.right = invert_tree(head.right)
    return head