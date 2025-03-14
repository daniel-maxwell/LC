class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {

        unordered_map<int, vector<int>> studentScores;
        unordered_set<int> students;

        for (const vector<int> &score : items) {
            studentScores[score[0]].push_back(score[1]);
            students.insert(score[0]);
        }

        vector<vector<int>> result;

        for (const vector<int> &score : items) {
            const int studentID = score[0];
            if (students.contains(studentID)) {
                sort(studentScores[studentID].begin(), studentScores[studentID].end());
                int sum = 0;
                for (int i = 0; i < 5; ++i) {
                    sum += studentScores[studentID].back();
                    studentScores[studentID].pop_back();
                }
                result.push_back(vector<int>{studentID, sum / 5});
                students.erase(studentID);
            }
        }

        sort(result.begin(), result.end());
        
        return result;
    }
};