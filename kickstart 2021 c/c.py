t = int(input())
x = int(input())
a = 'RPS'

for test_idx in range(1,t+1):
    w,e = map(int, input().split(' '))

    dp = [[[-100]*61 for _ in range(61)] for __ in range(61)]
    resa = [[['']*61 for _ in range(61)] for __ in range(61)]
    dp[1][0][0] = 1/3*w+1/3*e
    dp[0][1][0] = 1/3*w+1/3*e
    dp[0][0][1] = 1/3*w+1/3*e
    resa[1][0][0] = 0
    resa[0][1][0] = 1
    resa[0][0][1] = 2

    cmax = -1000
    cval = [0,0,0]
    for n in range(2,61):
        for j in range(n):
            for k in range(n-j):
                i = n-j-k
                if i > 0 and dp[i][j][k] < dp[i-1][j][k] + j/(n-1)*w + k/(n-1)*e:
                    dp[i][j][k] = dp[i-1][j][k] + j/(n-1)*w + k/(n-1)*e
                    resa[i][j][k] = 0
                if j > 0 and dp[i][j][k] < dp[i][j-1][k] + k/(n-1)*w + i/(n-1)*e:
                    dp[i][j][k] = dp[i][j-1][k] + k/(n-1)*w + i/(n-1)*e
                    resa[i][j][k] = 1
                if k > 0 and dp[i][j][k] < dp[i][j][k-1] + i/(n-1)*w + j/(n-1)*e:
                    dp[i][j][k] = dp[i][j][k-1] + i/(n-1)*w + j/(n-1)*e
                    resa[i][j][k] = 2

                if n == 60 and dp[i][j][k] > cmax:
                    cmax = dp[i][j][k]
                    cval = [i,j,k]
    res = ''
    for i in range(60):
        res += 'RPS'[resa[cval[0]][cval[1]][cval[2]]]
        cval[resa[cval[0]][cval[1]][cval[2]]] -= 1

    print("Case #%i: %s" % (test_idx, res[::-1]))
