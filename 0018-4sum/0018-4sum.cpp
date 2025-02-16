class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        const int n = nums.size();

        if (n < 4) return vector<vector<int>>{};
        
        sort(nums.begin(), nums.end());

        vector<vector<int>> result;
        unordered_map<long long, vector<int>> numMap;

        for (int i = 0; i < nums.size(); ++i) {
            numMap[(long long)nums[i]].push_back(i);
        }

        unordered_set<string> quadruplets;

        for (int i = 0; i < nums.size() - 3; ++i) {
            for (int j = i + 1; j < nums.size() - 2; ++j) {
                for (int k = j + 1; k < nums.size() - 1; ++k) {
                    const long long currSum = (long long)nums[i] + (long long)nums[j] + (long long)nums[k];
                    const long long currTarget = getCurrTarget(currSum, (long long)target);

                    if (numMap.contains(currTarget)) {
                        bool validIdx = false;

                        for (const int &idx : numMap[currTarget]) {
                            if (idx != i && idx != j && idx != k) {
                                validIdx = true;
                                break;
                            }
                        }

                        if (!validIdx) continue;
                        vector<int> candidate {nums[i], nums[j], nums[k], int(currTarget)};
                        sort(candidate.begin(), candidate.end());
                        const string serialized = to_string(candidate[0]) + "," + 
                                                  to_string(candidate[1]) + "," + 
                                                  to_string(candidate[2]) + "," + 
                                                  to_string(candidate[3]);

                        if (!quadruplets.contains(serialized)) {
                            result.push_back(candidate);
                            quadruplets.insert(serialized);
                        }
                    }
                }
            }
        }
        return result;
    }

    const long long getCurrTarget(const long long currSum, const long long target) {
        return target - currSum;
    }
};