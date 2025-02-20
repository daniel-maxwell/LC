/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
static const bool init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return false;
}();
class Solution {
public:
    const vector<vector<int>> pathSum(const TreeNode* root, const int targetSum) {

        if (root == nullptr) return result;

        if (root->left == nullptr && root->right == nullptr) { // leaf
            currSum += root->val;
            path.push_back(root->val);
            if (currSum == targetSum) result.push_back(path);
            currSum -= root->val;
            path.pop_back();
            return result;
        }

        currSum += root->val;
        path.push_back(root->val);

        pathSum(root->left, targetSum);
        pathSum(root->right, targetSum);

        currSum -= root->val;
        path.pop_back();

        return result;
    }

    int currSum = 0;
    vector<int> path;
    vector<vector<int>> result;
};