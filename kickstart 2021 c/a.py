MOD = 1000000007

t = int(input())
for test_idx in range(1,t+1):
    n, k = map(int, input().split(' '))
    s = input()

    max_idx = (n-1)//2

    res = 0

    num_ahead = 1

    for j in range(max_idx-1,-1,-1):
        curr_val= s[j]
        num_ahead = (num_ahead *k) % MOD
        cres = ((ord(curr_val) - ord('a')) * num_ahead) % MOD
        res = (res+cres) % MOD

    final_string = ['']*n
    for j in range(max_idx+1):
        final_string[j] = s[j]
        final_string[n-1-j] = s[j]

    final_string = ''.join(final_string)
    res = (res + ord(s[max_idx]) - ord('a')) % MOD

    if final_string < s:
        res = (res+1) % MOD

    print("Case #%i: %i" % (test_idx, res))
