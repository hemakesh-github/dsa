#include<bits/stdc++.h>

using namespace std;


bool pushBalls(int n, int m, vector<string> mat) {
    vector<vector<int>> tempMat(n, vector<int>(m, 0));
    for (int j = 0; j<m; j++){
        int s = 0;
        for (int i= 0; i < n; i++) {
            if (mat[i][j] == '1') {
                s++;
            }
            tempMat[i][j] = s;
        }
    }

    for (int i = 0; i < n; i++) {
        int s = 0;
        for (int j = 0; j < m; j++) {
            
            if (mat[i][j] == '1'){
                s+=1;
            }

            if (mat[i][j] == '1' && (tempMat[i][j] != i+1 && s != j+1)) {

                return false;
            }

        }
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    vector<bool> ans;
    for (int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;
        vector<string> mat;
        for (int j = 0; j < n; j++) {
            string s;
            cin >> s;
            mat.push_back(s);
        }
        ans.push_back(pushBalls(n, m, mat));
    }
    for (auto i: ans) {
        if (i) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}