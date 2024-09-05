def eliminate_rep(a):
    char = a[0]
    char_cnt = 1
    for i in range(1, len(a)):
        if a[i] == char:
            char_cnt += 1
        else:
            char = a[i]
            char_cnt = 1
        if char_cnt > 2:
            a[i] = ''
            return a
        elif char_cnt == 2:
            if i + 2 < len(a):
                if a[i+1] == a[i+2]:
                    a[i+2] = ''
                    return a
    return a
    
if __name__ == "__main__":
    s = "yyybeettxjjjpppddsrxxxkkkyyyooowwwwwkyyxxppplllwwwiivvssnrvvvccclyydddhaaayiic"
    # yybeetxjjpddsrxxkyyowwkyyxpplwwivvsnrvvclyydhaayiic
    a = "".join(eliminate_rep(list(s)))
    while (a != "".join(eliminate_rep(list(a)))):
        a = "".join(eliminate_rep(list(a)))
    print(a)