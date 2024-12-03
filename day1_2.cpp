// DAY 1: PART 2

#include <iostream>
#include <fstream>
#include <unordered_map>

using namespace std;
ifstream fin("day1.txt");

unordered_map<int, int> a;
unordered_map<int, int> b;

int main() {
    int i;
    int j;
    fin >> i >> j;
    while (!fin.eof()) {
        if (a.find(i) == a.end()) { a[i] = 1; }
        else { a[i] ++; }

        if (b.find(j) == b.end()) { b[j] = 1; }
        else { b[j] ++; }

        fin >> i >> j;
    }
    
    int s = 0;

    for (unordered_map<int, int>::iterator it = a.begin(); it != a.end(); it++) {
      int n = it->first;
      if (b.find(n) != b.end()) {
        s += n * a[n] * b[n];
      }
    }
    
    cout << s << endl;

    return 0;
}
