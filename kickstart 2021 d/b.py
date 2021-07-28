from collections import defaultdict
t = int(input())

for test_idx in range(1,t+1):
    n, c = map(int, input().split(' '))

    cl = defaultdict(int)
    for i in range(n):
        s, e = map(int, input().split(' '))
        s += 1
        cl[s] += 1
        cl[e] -= 1

    ck = sorted(cl.keys())
    cv = [cl[val] for val in ck]

    csum = [0]
    for v in cv:
        csum.append(csum[-1]+v)
    csum = csum[1:-1]

    range_list = [(ck[idx+1]-ck[idx],csum[idx]) for idx in range(len(ck)-1) if csum[idx] > 0]
    range_list.sort(key = lambda x: x[1], reverse=True)
    range_ptr = 0

    while range_ptr < len(range_list) and c:
        curr_amt, curr_size = range_list[range_ptr]
        if curr_amt <= c:
            n += curr_amt * curr_size
            c -= curr_amt
            range_ptr += 1
        else:
            n += c * curr_size
            c = 0
    print("Case #%i: %i" % (test_idx, n))
