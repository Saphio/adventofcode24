// DAY 1: PART 1

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;
ifstream fin("day1.txt");


vector<int> a;
vector <int> b;

int main() {
    int i;
    int j;
    // cin >> i >> j;
    fin >> i >> j;
    while (!fin.eof()) {
        a.push_back(i);
        b.push_back(j);
        // cin >> i >> j;
        fin >> i >> j;
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
