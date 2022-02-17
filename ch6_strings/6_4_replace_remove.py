def replace_and_remove(size: int, s: [str]) -> int:
    write_idx, a_count = 0, 0
    # need to remove b entries
    for i in range(size):
        ch = s[i]
        if ch == "a":
            a_count += 1
        if ch != 'b':
            s[write_idx] = ch
            write_idx += 1
    # current idx for the original entries
    cur_idx = write_idx - 1
    # write entries, insert from back
    write_idx += a_count - 1
    ans = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx -1:write_idx+1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return ans

arr = ['b','c','a','a','','','','','','','']
print(replace_and_remove(4, arr))
print(arr)