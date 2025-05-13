class Solution {
public:
    const int numRookCaptures(const vector<vector<char>>& board) {

        pair<int, int> rookCoord;

        for (int r = 0; r < 8; ++r) {
            bool found = false;
            for (int c = 0; c < 8; ++c) {
                if (board.at(r).at(c) == 'R') {
                    rookCoord = pair<int, int>{r, c};
                    found = true;
                    break;
                }
            }
            if (found) break;
        }

        int result = 0;

        pair<int, int> curr = rookCoord;
        --curr.first;
        while (curr.first >= 0) {
            if (board.at(curr.first).at(curr.second) == 'p') {
                ++result;
                break;
            } else if (board.at(curr.first).at(curr.second)!= '.') {
                break;
            }
            --curr.first;
        }
        curr = rookCoord;
        ++curr.second;
        while (curr.second < 8) {
            if (board.at(curr.first).at(curr.second) == 'p') {
                ++result;
                break;
            } else if (board.at(curr.first).at(curr.second) != '.') {
                break;
            }
            ++curr.second;
        }
        curr = rookCoord;
        ++curr.first;
        while (curr.first < 8) {
            if (board.at(curr.first).at(curr.second) == 'p') {
                ++result;
                break;
            } else if (board.at(curr.first).at(curr.second) != '.') {
                break;
            }
            ++curr.first;
        }
        curr = rookCoord;
        --curr.second;
        while (curr.second >= 0) {
            if (board.at(curr.first).at(curr.second) == 'p') {
                ++result;
                break;
            } else if (board.at(curr.first).at(curr.second) != '.') {
                break;
            }
            --curr.second;
        }

        return result;
    }
};