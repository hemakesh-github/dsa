#include<bits/stdc++.h>

using namespace std;

bool treasure(double x, double y, double a) {
    long long n = floor((a+0.5)/(x+y)) + 1;
    if (n*x + (n-1)*y > a) {
        return false;
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    vector<bool> ans;
    for (int i = 0; i < t; i++) {
        double x, y, a;
        cin >> x >> y >> a;
        ans.push_back(treasure(x, y, a));
    }

    for (auto i: ans) {
        if (i) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

}


