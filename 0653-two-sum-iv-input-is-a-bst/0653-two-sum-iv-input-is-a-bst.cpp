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
    bool findTarget(TreeNode* root, const int k) {
        if (root == nullptr) return false;
        const bool result = visited.contains(k - root->val);
        visited.insert(root->val);
        return result || findTarget(root->left, k) || findTarget(root->right, k);
    }
    unordered_set<int> visited;
};