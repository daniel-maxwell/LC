class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        
        vector<int> sortedScores = score;
        sort(sortedScores.begin(), sortedScores.end());

        unordered_map<int, string> scoreToPlacement;
        for (int i = 0; i < sortedScores.size(); ++i) {
            string placement = to_string(sortedScores.size() - i);
            if (placement == "1") {
                placement = "Gold Medal";
            } else if (placement == "2") {
                placement = "Silver Medal";
            } else if (placement == "3") {
                placement = "Bronze Medal";
            }
            scoreToPlacement[sortedScores[i]] = placement;
        }

        vector<string> result;
        for (const int &s : score) {
            result.push_back(scoreToPlacement[s]);
        }

        return result;
    }
};