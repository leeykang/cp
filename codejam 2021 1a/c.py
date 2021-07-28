from fractions import Fraction

def ot(c):
	return 'T' if c == 'F' else 'F'

def C(n, k):
	res = 1
	for i in range(k):
		res = res * (n - i) // (i + 1)
	return res

def repr(x):
	return str(x) if x.denominator > 1 else str(x) + "/1"

def solve():
	n, q = map(int, input().split())
	a = []
	sc = []
	for i in range(n):
		line = input().split()
		a.append(line[0])
		sc.append(int(line[1]))

	by_mask = [[] for i in range(2 ** (n - 1))]
	for i in range(q):
		mask = 0
		for j in range(n - 1, 0, -1):
			mask = mask * 2 + int(a[j][i] != a[0][i])
		by_mask[mask].append(i)

	for i in range(n):
		sc[i] = q - sc[i]
	es = [0 for i in range(2 ** len(by_mask))]
	ways = 0
	for c in range(q + 1):
		cs = [0] * len(by_mask)
		cs[-1] = c
		if n == 3:
			for i in range(1, n):
				tmp = (sum(len(by_mask[j]) for j in range(len(by_mask)) if (j & (1 << (i - 1))) > 0) - sc[i] + sc[0]) // 2
				cs[2 ** (i - 1)] = tmp - c
		if n > 1:
			cs[0] = sc[0] - sum(cs)
		fail = False
		if sum(cs) != sc[0]:
			fail = True
		for i in range(1, n):
			tmp = 0
			for j in range(len(by_mask)):
				tmp += cs[j] if (j & (1 << (i - 1)) == 0) else len(by_mask[j]) - cs[j]
			if tmp != sc[i]:
				fail = True
		for i in range(len(by_mask)):
			if not 0 <= cs[i] <= len(by_mask[i]):
				fail = True
				break
		if fail:
			continue

		cw = 1
		for i in range(len(by_mask)):
			cw *= C(len(by_mask[i]), cs[i])
		ways += cw
		for mask in range(len(es)):
			csc = 0
			for i in range(len(by_mask)):
				csc += cs[i] if (mask & (1 << i)) == 0 else len(by_mask[i]) - cs[i]
			es[mask] += csc * cw

	opt = (10**1000, "abcde")
	for mask in range(len(es)):
		s = [c for c in a[0]]
		for i in range(len(by_mask)):
			if mask & (1 << i):
				for idx in by_mask[i]:
					s[idx] = ot(s[idx])
		opt = min(opt, (Fraction(es[mask], ways), "".join(s)))
	print(opt[1], repr(q - opt[0]))

t = int(input())
for i in range(t):
	print("Case #{}:".format(i + 1), end=' ')
	solve()
