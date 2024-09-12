class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        vector<vector<int>> resImg = img;
        const vector<pair<int, int>> directions {
            {0, 0},
            {-1, 0},
            {-1, 1},
            {0, 1},
            {1, 1},
            {1, 0},
            {1, -1},
            {0, -1},
            {-1, -1}
        };
        for (int i = 0; i < img.size(); ++i) {
            for (int j = 0; j < img[0].size(); ++j) {
                int numValues = 0;
                int sumTotal = 0;
                for (pair<int, int> dir : directions) {
                    const pair<int, int> move {i + dir.first, j + dir.second};
                    if (isValidCoord(move, img.size(), img[0].size())) {
                        ++numValues;
                        sumTotal += img[i + dir.first][j + dir.second];
                    }
                }
                resImg[i][j] = sumTotal / numValues;
            }
        }
        return resImg;
    }
    bool isValidCoord(const pair<int, int> coord, const int rows, const int cols) {
        if (
            coord.first < 0 ||
            coord.second < 0 ||
            coord.first >= rows ||
            coord.second >= cols
        ) {
            return false;
        }
        return true;
    }
};