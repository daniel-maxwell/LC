class Solution {
public:
  set<pair<int, int>> island1;
  set<pair<int, int>> visited;
  
  int shortestBridge(vector<vector<int>> &grid) {
    const int ROWS = grid.size();
    const int COLS = grid[0].size();
    bool found = false;
    for (int row = 0; row < ROWS; ++row) {
      for (int col = 0; col < COLS; ++col) {
        if (grid[row][col] == 1) {
          island1 = getIslandCoords(grid, pair<int, int>{row, col}, ROWS, COLS);
          found = true;
          break;
        }
      }
      if (found) break;
    }
    return calcShortestBridge(grid, ROWS, COLS);
  }

  set<pair<int, int>> getIslandCoords(const vector<vector<int>> &grid, const pair<int, int> &coord, const int ROWS, const int COLS) {
    const vector<pair<int, int>> directions{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    queue<pair<int, int>> q;
    q.push(coord);
    set<pair<int, int>> result;
    visited.insert(coord);
    
    while (!q.empty()) {
      const pair<int, int> curr = q.front();
      q.pop();
      
      result.insert(curr);

      for (const pair<int, int> &diff : directions) {
        pair<int, int> move { curr.first + diff.first, curr.second + diff.second };
        
        if (move.first < 0 || move.first == ROWS || move.second < 0 || move.second == COLS || visited.contains(move) || grid[move.first][move.second] == 0) {
          continue;
        }
        
        q.push(move);
        visited.insert(move);
      }
    }
    
    return result;
  }

  int calcShortestBridge(const vector<vector<int>> &grid, const int ROWS, const int COLS) {
    const vector<pair<int, int>> directions{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    queue<pair<int, int>> q;
    
    for (const pair<int, int> coord : island1) {
      q.push(coord);
    }
    
    int dist = 0;
    
    while (!q.empty()) {
      int size = q.size();
      
      for (int i = 0; i < size; ++i) {
        pair<int, int> coord = q.front();
        q.pop();
        
        for (const pair<int, int> &diff : directions) {
          pair<int, int> move { coord.first + diff.first, coord.second + diff.second };
          
          if (move.first < 0 || move.first == ROWS || move.second < 0 || move.second == COLS || visited.contains(move)) {
            continue;
          }

          if (grid[move.first][move.second] == 1) {
            return dist;
          }
          
          q.push(move);
          visited.insert(move);
        }
      }
      ++dist;
    }
    return -1;
  }
};
