// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
#include <algorithm>
// #include <fstream>

// ifstream fin("input1.txt");

using namespace std;

vector<int> a;
vector <int> b;

int main() {
    int i;
    int j;
    cin >> i >> j;
    while (i != -1) {
        a.push_back(i);
        b.push_back(j);
        cin >> i >> j;
    }
    
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    int s = 0;
    
    for (int i = 0; i < a.size(); i++) {
        s += abs(a[i] - b[i]);
    }
    
    cout << s << endl;

    return 0;
}
