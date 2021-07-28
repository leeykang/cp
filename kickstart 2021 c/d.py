import sys
input = sys.stdin.readline

t = int(input().strip())
for test_idx in range(1,t+1):
    n = int(input().strip())
    arr = [input().strip() for i in range(n)]

    cptr = 1
    cd = {}
    fullres = [0]*n

    for idx, val in enumerate(arr):
        fres = []
        for c in ['+','-','^','|','&','^1111+1000000007+1111^','^1110+1000000007+1110^','+1000000007+','>>','-1000000007+','%1000000007+','%1000000007-','+1000000007-','-1000000007-','*0+1000000007+0*','//2+14621984+0*','//3+347387343+2*','//154+14621984+0*','//348+347387343+2*','*2+14621984+0*','*3+347387343+2*']:
            req = val.replace('#',c)
            x = eval(req)
            fres.append(x)

        if tuple(fres) not in cd:
            cd[tuple(fres)] = str(cptr)
            cptr += 1
        fullres[idx] = cd[tuple(fres)]

    print("Case #%i:" % test_idx, ' '.join(fullres))
