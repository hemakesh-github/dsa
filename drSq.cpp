#include<bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    vector<string> ans;
    for(int i = 0; i < t; i++) {
        int l, r, d, u;

        cin >> l >> r >> d >> u;
        
        if ((l == r) && (r==d) && (d == u)) {
            ans.push_back("YES");
        } else {
            ans.push_back("NO");
        }
    }

    for (int i = 0; i < t; i++){
        cout << ans[i] << endl;
    }
}

