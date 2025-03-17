def rotate_right(head, k):
    
    if head is None:
        return None
    
    if k == 0:
        return head
    
    list_len = 0
    orig_head = head
    last = None
    new_head = None
    
    while head:
        list_len += 1
        head = head.next
    
    if list_len == 1 or k == list_len:
        return orig_head
    
    head = orig_head
    
    step = 0
    while head:
        step += 1
        curr = head
        if head.next is None:
            last = head
        head = head.next
        if step == list_len - k:
            new_head = curr.next
            curr.next = None
            
    last.next = orig_head
        
    return new_head