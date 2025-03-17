def is_subsequence(s, t):
    if s is None or len(s) == 0 or t is None or len(t) == 0:
        return False
    s_ind = 0
    for t_char in t:
        if t_char == s[s_ind]:
            s_ind += 1
            if s_ind == len(s):
                return True

    if s_ind == len(s):
        return True
    else:
        return False