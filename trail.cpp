#include <bits/stdc++.h>

using namespace std;

vector<vector<long long int>> trail(int m, int n,vector<vector<long long int>> matrix, string path){
    int i = 0, j = 0;
    for (char p: path) {
        if (p == 'D'){
            long long x = 0;
            for (int k = 0; k < n; k++){
                x += matrix[i][k];
            }
            matrix[i][j] = -x;
            i+=1;
        } else {
            long long x = 0;
            for (int k = 0; k<m; k++) {
                x += matrix[k][j];
            }
            matrix[i][j] = -x;
            j+=1;
        }
    }
    long long x = 0;
    if (m < n) {
        for (int k = 0; k < m; k++) {
            x += matrix[k][j];
        }
        matrix[i][j] = -x;
    } else {
        for (int k = 0; k < n; k++) {
            x += matrix[i][k];
        }
        matrix[i][j] = -x;
    }
    return matrix;
}

int main() {
    int t;
    cin >> t;
    vector<vector<vector<long long int>>> ans = {};

    for(int i = 0; i < t; i++) {
        int m, n;
        cin >> m >> n;
        string path;
        cin >> path;
        vector<vector<long long int>> matrix = {};
        for(int j = 0; j < m; j++){
            vector<long long int> v = {};
            for(int k = 0; k < n; k++) {
                long long int val;
                cin >> val;
                v.push_back(val);
            }
            matrix.push_back(v);
        }
        ans.push_back(trail(m, n, matrix, path));
    }

    for(int i = 0; i < t; i++){
        for (int j = 0; j < ans[i].size(); j ++){
            for (int k = 0; k < ans[i][j].size(); k ++) {
                cout << ans[i][j][k] << " ";
            }
            cout << "\n";
        }
    }

}
