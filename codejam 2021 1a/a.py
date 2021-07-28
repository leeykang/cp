t = int(input())
for j in range(1,t+1):
    n = int(input())
    arr = [int(val) for val in input().split(' ')]
    arrs = [str(val) for val in arr]
    digits = sum(len(val) for val in arrs)

    resarr = [arr[0]]
    resarrs = [arrs[0]]

    for i in range(1,n):
        c_num = arr[i]
        c_str = arrs[i]

        if c_num > resarr[-1]:
            resarr.append(c_num)
            resarrs.append(c_str)
        elif c_num == resarr[-1]:
            resarr.append(c_num * 10)
            resarrs.append(str(resarr[-1]))
        else:
            pnd = len(resarrs[-1])
            pcd = len(c_str)
            if pnd == pcd:
                resarr.append(c_num * 10)
                resarrs.append(str(resarr[-1]))
            else:
                min_s = c_str + '0' * (pnd-pcd)
                max_s = c_str + '9' * (pnd-pcd)
                min_val = int(min_s)
                max_val = int(max_s)

                if max_val <= resarr[-1]:
                    resarrs.append(min_s+'0')
                    resarr.append(int(resarrs[-1]))
                elif min_val > resarr[-1]:
                    resarr.append(min_val)
                    resarrs.append(min_s)
                else:
                    resarr.append(resarr[-1]+1)
                    resarrs.append(str(resarr[-1]))

    new_digits = sum(len(val) for val in resarrs)

    print("Case #%i: %i" % (j,new_digits-digits))
