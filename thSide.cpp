#include<bits/stdc++.h>

using namespace std;


int thSide(int n, vector<int> a) {
    int ans = 0;
    for (auto e: a) {
        ans+=e;
    }
    return ans - (n-1);
}
int main() {
    int t;
    cin >> t;
    vector<int> ans;
    for (int i = 0; i < t; i++){
        int n;
        vector<int> a;
        cin >> n;
        for (int j = 0; j < n; j++) {
            int x;
            cin >> x;
            a.push_back(x);
        }
        ans.push_back(thSide(n, a));
    }

    for (auto a: ans) {
        cout << a << endl;
    }

    
}
