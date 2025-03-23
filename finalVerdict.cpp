#include<bits/stdc++.h>
using namespace std;

bool finalVerdict(int n, int x, vector<int> a) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i];
    }
    if (sum%n != 0){
        return false;
    }
    return (x == (sum/n));
}

int main() {
    int t;
    cin >> t;
    vector<bool> ans;
    for (int i = 0; i < t; i++) {
        int n, x;
        cin >> n;
        cin >> x;
        vector<int> vec(n);
        for (int i = 0; i < n; i++) {
            cin >> vec[i];
        }
        ans.push_back(finalVerdict(n, x, vec));

    }

    for (int i = 0; i < t; i++) {
        if (ans[i]) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}