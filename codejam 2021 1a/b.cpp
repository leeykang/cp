#include <bits/stdc++.h>
using namespace std;


typedef long long ll;
typedef map<ll,ll> mllll;

#define REPL(i,a,b) for (long long i = (a); i < (b); ++i)

void solve() {
    ll m, j, n, p, ts=0, rs, cval, ns, ss;
    cin >> m;
    mllll cm, cm2, cm3;
    set<ll> cs;
    REPL(j,0,m) {
        cin >> p >> n;
        cm[p] = n;
        ts += p*n;
        cs.insert(p);
    }
    bool is_valid;
    for (ll k = ts-2; k >= ts-30000 && k >= 2; --k) {
        cm2 = cm3;
        is_valid = true;
        ss = k;
        rs = ts-k;
        for (const auto &c: cs) {
            cval = cm[c];
            while (cval && ss % c == 0) {
                ++cm2[c];
                ss /= c;
                --cval;
            }
            if (ss % c == 0) {
                is_valid = false;
                break;
            }
        }
        if (ss > 1) {
            continue;
        }
        if (is_valid) {
            ns = 0;
            for (const auto &kv: cm2) {
                ns += kv.first * kv.second;
            }
            if (ns == rs) {
                cout << k << "\n";
                return;
            }
        }

    }
    cout << "0\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
	}

	return 0;
}
