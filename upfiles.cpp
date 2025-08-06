#include<bits/stdc++.h>

using namespace std;

long long upfiles(long long n, long long k) {
    long long s, ans=0;
    long long x = ceil(log2l(k));
    
    ans += x;
    s = pow(2, x);
    cout << x << " " << s << " " << ans << " " << n-s << endl;
    if (n > s) {
        ans += (n-s)/k;
        if ((n-s)%k != 0) {
            ans++;
        }
    }
    return ans;
}

int main() {
    int t;
    cin >> t;
    vector<long long> ans;
    for (int i = 0; i < t; i++) {
        long long n, k;
        cin >> n >> k;

        ans.push_back(upfiles(n, k));
    }

    for (auto a: ans) {
        cout << a << endl;
    }
}