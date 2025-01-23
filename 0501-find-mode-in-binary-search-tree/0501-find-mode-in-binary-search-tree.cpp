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
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        dfs(root);
        vector<int> result;
        for (const auto &entry : counts) {
            if (entry.second == maxOcc) {
                result.push_back(entry.first);
            }
        }
        return result;
    }

    void dfs(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        ++counts[root->val];
        maxOcc = max(maxOcc, counts[root->val]);
        dfs(root->left);
        dfs(root->right);
    }

    int maxOcc = -1;
    unordered_map<int, int> counts;
};