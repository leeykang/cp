from collections import defaultdict
t = int(input())
for test_idx in range(1,t+1):
    mat = [[0]*3 for __ in range(3)]
    mat[0] = list(map(int, input().split(' ')))
    mat[1][0], mat[1][2] = map(int, input().split(' '))
    mat[2] = list(map(int, input().split(' ')))

    cd = defaultdict(int)

    first_sum = mat[0][0] + mat[2][2]
    first_val = first_sum//2
    if first_val * 2 == first_sum:
        cd[first_val] += 1

    first_sum = mat[0][1] + mat[2][1]
    first_val = first_sum//2
    if first_val * 2 == first_sum:
        cd[first_val] += 1

    first_sum = mat[2][0] + mat[0][2]
    first_val = first_sum//2
    if first_val * 2 == first_sum:
        cd[first_val] += 1

    first_sum = mat[1][0] + mat[1][2]
    first_val = first_sum//2
    if first_val * 2 == first_sum:
        cd[first_val] += 1

    if not cd:
        max_count = 0
    else:
        max_val = max(cd.keys(), key=lambda x: cd[x])
        max_count = cd[max_val]

    if mat[0][1] - mat[0][0] == mat[0][2] - mat[0][1]:
        max_count += 1

    if mat[1][0] - mat[0][0] == mat[2][0] - mat[1][0]:
        max_count += 1

    if mat[2][1] - mat[2][0] == mat[2][2] - mat[2][1]:
        max_count += 1

    if mat[1][2] - mat[0][2] == mat[2][2] - mat[1][2]:
        max_count += 1

    print("Case #%i: %i" % (test_idx, max_count))
