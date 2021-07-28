#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<ll> vll;
typedef pair<ll,ll> pll;
typedef map<int,int> mii;
typedef map<ll,ll> mllll;
typedef map<int, vi> mivi;
typedef map<ll, vll> mllvll;

#define F first
#define S second
#define PB push_back
#define MP make_pair

#define SV(v) sort((v).begin(), (v).end())
#define REP0(a,b) for (int i = (a); i <= (b); ++i)
#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPL0(a,b) for (int i = (a); i < (b); ++i)
#define REPL(i,a,b) for (int i = (a); i < (b); ++i)

#define DTI(a) (int)((a)-'0')
#define LATI(a) (int)((a)-'a')
#define UATI(a) (int)((a)-'A')

void read_arri(int &n, vi &arr) {
    int k;
    REPL0(0,n) {
        cin >> k;
        arr.PB(k);
    }
}

void read_arrll(int &n, vll &arr) {
    ll k;
    REPL0(0,n) {
        cin >> k;
        arr.PB(k);
    }
}

//struct P {
//    int x, y;
//    bool operator<(const P &p) {
//        if (x != p.x) return x < p.x;
//        else return y < p.y;
//    }
//};

//bool comp(string a, string b) {
//    if (a.size() != b.size()) return a.size() < b.size();
//    return a < b;
//}
//sort(v.begin(), v.end(), comp);

//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);

//printf("%.9f\n", x);

// x %= m;
// if (x < 0) x += m;

void solve() {
    int n, m;
    ll a, b, s;
    cin >> n >> m;

    int j;
    mllll cm;

    REPL(j,0,n) {
        cin >> a >> b;
        cm[a] = b;
    }

    REPL(j,0,m) {
        cin >> s;
        auto res = cm.upper_bound(s);
        if (res == cm.begin()) {
            a = res->first;
            if (a+1 <= cm[a]) {
                cm[a+1] = cm[a];
            }
            cm.erase(a);
            cout << a << " ";
        }
        else {
            auto res2 = res;
            res2--;
            a = res2->first;
            if (a <= s && s <= cm[a]) {
                cout << s << " ";
                if (s+1 <= cm[a]) {
                    cm[s+1] = cm[a];
                }
                if (a <= s-1) {
                    cm[a] = s-1;
                }
                else {
                    cm.erase(a);
                }
            }
            else if (res == cm.end()) {
                cout << cm[a] << " ";
                if (a <= cm[a]-1) {
                    --cm[a];
                }
                else {
                    cm.erase(a);
                }
            }
            else {
                a = res2->first;
                b = res->first;
                if (s - cm[a] <= b - s) {
                    cout << cm[a] << " ";
                    if (a<= cm[a]-1) {
                        --cm[a];
                    }
                    else {
                        cm.erase(a);
                    }
                }
                else {
                    cout << b << " ";
                    if (b+1 <= cm[b]) {
                        cm[b+1] = cm[b];
                    }
                    cm.erase(b);
                }
            }
        }
    }
    cout << "\n";
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
