def are_trees_equal(head_1, head_2):
    equal = True
    if (head_1 is not None and head_2 is None) or \
        (head_1 is None and head_2 is not None) or \
        (head_1 is not None and head_2 is not None and head_1.val != head_2.val):
        equal = False
    if equal and head_1 is not None and head_2 is not None:
        equal = are_trees_equal(head_1.left, head_2.left)
        if equal:
            equal = are_trees_equal(head_1.right, head_2.right)
    return equal