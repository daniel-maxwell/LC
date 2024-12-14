class TicTacToe {
public:
    TicTacToe(int n) {
        for (int i = 0; i < n; ++i) {
            rows.push_back(pair<int, int>{0, n});
            cols.push_back(pair<int, int>{0, n});
        }
        leftDiag = pair<int, int>{0, n};
        rightDiag = pair<int, int>{0, n};
    }
    
    int move(int row, int col, int player) {

        if (rows[row].first == player || rows[row].first == 0) {
            rows[row].first = player;
            --rows[row].second;
            if (rows[row].second == 0) return player;
        } else {
            rows[row].first = -1;
            rows[row].second = -1;
        }


        if (cols[col].first == player || cols[col].first == 0) {
            cols[col].first = player;
            --cols[col].second;
            if (cols[col].second == 0) return player;
        } else {
            cols[col].first = -1;
            cols[col].second = -1;
        }

        if (row == col) {
            if (leftDiag.first == player || leftDiag.first == 0) {
                leftDiag.first = player;
                --leftDiag.second;
                if (leftDiag.second == 0) return player;
            } else {
                leftDiag.first = -1;
                leftDiag.second = -1;
            }
        }

        if (row + col == rows.size() - 1) {
            if (rightDiag.first == player || rightDiag.first == 0) {
                rightDiag.first = player;
                --rightDiag.second;
                if (rightDiag.second == 0) return player;
            } else {
                rightDiag.first = -1;
                rightDiag.second = -1;
            }
        }
        
        return 0;
    }

    vector<pair<int, int>> rows; // player, remaining
    vector<pair<int, int>> cols;
    pair<int, int> leftDiag;
    pair<int, int> rightDiag;

};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */