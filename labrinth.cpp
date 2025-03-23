#include<bits/stdc++.h>
using namespace std;

vector<int> labr(int n, int k) {
    vector<int> ans;
    if (k%2 == 0) {
        for(int i = 0; i < n - 2;i++) {
            ans.push_back(n-1);
        }
        ans.push_back(n);
        ans.push_back(n-1);

    } else {
        for (int i = 0; i < n-1; i++) {
            ans.push_back(n);
        }
        ans.push_back(n-1);
    }
    return ans;
}


int main() {
    int t;
    cin >> t;
    vector<vector<int>> ans;
    for (int i = 0; i < t; i++) {
        int n, k;
        cin >> n;
        cin >> k;
        
        ans.push_back(labr(n, k));

    }

    for (int i = 0; i < t; i++) {
        for (auto x: ans[i]) {
            cout << x << " ";
        }
        cout << endl;
    }
}