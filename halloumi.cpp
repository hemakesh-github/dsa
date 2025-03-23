#include <bits/stdc++.h>
using namespace std;

string halloumi(int n, int t, vector<int> vec) {
    int cnt = 1;
    if (t <= 1) {
        for (int i = 1; i < n; i++) {
            if (vec[i-1] <= vec[i]) {
                cnt++;
            }
        }
        if (cnt == n) {
            return "YES";
        }
        return "NO";
    }
    return "YES";
}

int main(){
    vector<string> ans = {};
    int tests;
    cin >> tests;
    for (int i = 0; i < tests; i++) {
        int n, t;
        cin >> n;
        cin >> t;
        vector<int> vec(n);
        for (int i = 0; i < n; i++) {
            cin >> vec[i];
        }
        ans.push_back(halloumi(n, t, vec));
    }

    for (const string res: ans){
        cout << res << endl;
    }
}

string clearDigits(string s) {
    vector<int> stk = {};

    for(int i = 0; i < s.length(); i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            if (stk.size() > 0) {
                stk.pop_back();
            }
        } else {
            stk.push_back(s[i]);
        }
    }
    return string(stk.begin(), stk.end())
}