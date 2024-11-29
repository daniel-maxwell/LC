class Solution {
public:
    vector<int> topStudents(vector<string>& positive_feedback,
                            vector<string>& negative_feedback,
                            vector<string>& report,
                            vector<int>& student_id,
                            int k) 
    {
        // Ranking: Points -> ID

        set<string> positiveWords;
        set<string> negativeWords;

        for (const string& f: positive_feedback) {
            positiveWords.insert(f);
        }

        for (const string& f: negative_feedback) {
            negativeWords.insert(f);
        }

        vector<pair<int, int>> studentScores;

        for (int i = 0; i < report.size(); ++i) {
            vector<string> sentence = split_sentence(report[i]);
            pair<int, int> studentScore {0, student_id[i]};
            for (const string& w: sentence) {
                if (positiveWords.contains(w)) {
                    studentScore.first += 3;
                } else if (negativeWords.contains(w)) {
                    --studentScore.first;
                }
            }
            studentScores.push_back(studentScore);
        }

        std::sort(studentScores.begin(), studentScores.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            if (a.first == b.first)
                return a.second < b.second;
            return a.first > b.first;
        });

        vector<int> result;
        for (int i = 0; i < k; ++i) {
            result.push_back(studentScores[i].second);
        }
        return result;

    }

    vector<string> split_sentence(string sen) {
        stringstream ss(sen);
        
        string word;
        
        vector<string> words;

        while (ss >> word) {
            words.push_back(word);
        }
        
        return words;
    }
};