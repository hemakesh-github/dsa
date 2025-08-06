#include <bits/stdc++.h>

using namespace std;
long long sumDamental(long long n , long long x){
    long long temp = x;
    long long z = 0, ans = 0, c = 0, vals = 0;
    while(c < n) {
        if (temp & 1) {
            ans += 1 << c;
            vals ^= 1 << c;
            // cout << ans << " " << vals << endl;
        } else {
            ans += 2 * (1<< c);
        }
        temp = temp >> 1;
        // cout << temp << endl;
        c++;
    }
    ans += ((~vals) & (x));
    return ans;
}

int main() {
    int t;
    cin >> t;
    vector<long long> ans;
    for (int i = 0; i < t; i++) {
        long long n, x;
        cin >> n >> x;
        ans.push_back(sumDamental(n, x));
    }

    for (auto a: ans) {
        cout << a << endl;
    }
    // cout<< sumDamental(2, 1);
}