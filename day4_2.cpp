// DAY 4: PART 2

#include <iostream>
#include <vector>
#include <fstream>
#include <cstring>

using namespace std;

ifstream fin("day4.txt");
vector<vector<char>> grid;

// checks 3x3 block for X-MAS
bool checkBlock (char block[3][3]) {
  if (block[0][0] == 'M' &&
      block[0][2] == 'M' &&
      block[1][1] == 'A' &&
      block[2][0] == 'S' &&
      block[2][2] == 'S') return true;
  if (block[0][0] == 'M' &&
    block[0][2] == 'S' &&
    block[1][1] == 'A' &&
    block[2][0] == 'M' &&
    block[2][2] == 'S') return true;
  if (block[0][0] == 'S' &&
    block[0][2] == 'S' &&
    block[1][1] == 'A' &&
    block[2][0] == 'M' &&
    block[2][2] == 'M') return true;
  if (block[0][0] == 'S' &&
    block[0][2] == 'M' &&
    block[1][1] == 'A' &&
    block[2][0] == 'S' &&
    block[2][2] == 'M') return true;
  return false;
}

int main () {
  int total;
  char c;

  // input
  char line[150];
  while (fin.getline(line, sizeof(line))) {
    vector<char> row;
    for (int i = 0; i < strlen(line); i++) {
      row.push_back(line[i]);
    }
    grid.push_back(row);
  }

  int rows = grid.size();
  int cols = grid[0].size();

  // check every possible block
  for (int r = 0; r < rows - 2; r++) {
    for (int c = 0; c < cols - 2; c++) {
      char block[3][3];
      block[0][0] = grid[r][c]; block[0][2] = grid[r][c + 2]; block[1][1] = grid[r + 1][c + 1]; block[2][0] = grid[r + 2][c]; block[2][2] = grid[r + 2][c + 2];
      if (checkBlock(block)) {
        total ++;
      }
    }
  }

  cout << total << endl;

  return 0;
}
