#include <bits/stdc++.h>
using namespace std;

int linetrip(int n, int x, vector<int> vec){
    int ans = vec[0];
    for (int i = 0; i < n - 1; i++) {
        ans = max(ans, vec[i+1] - vec[i]);
    }
    ans = max(ans, 2 * (x - vec[n-1]));
    return ans;
}

int main() {
    int t;
    cin >> t;
    vector<int> ans;
    for(int i = 0; i < t; i++) {
        int n, x;
        cin >> n;
        cin >> x;

        vector<int> vec(n);

        for (int i = 0; i < n; i++) {
            cin >> vec[i];
        }

        ans.push_back(linetrip(n, x, vec));
    }

    for (const int v: ans){
        cout << v << endl;
    }
}
