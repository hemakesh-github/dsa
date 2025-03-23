#include <bits/stdc++.h>

using namespace std;
int codeInWater(vector<char> inp){
    int i = 0, j, ans = 0;
    for(int j = 0; j <= inp.size(); j++){
        if (j == inp.size() || inp[j] == '#'){
            if ((j-i) >= 3) {
                return 2;
            }
            ans+=j-i;
            i = j+1;
        }
    }
    return ans ;

}

int main() {
    int t;
    cin >> t;
    vector<int> res;
    for(int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<char> inp(n);

        for (int j = 0; j < n; j++) {
            cin >> inp[j];
        }
        res.push_back(codeInWater(inp));

    }

    for (const int ans: res) {
        cout << ans << endl;
    }
}

