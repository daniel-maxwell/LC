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
    const int sumOfLeftLeaves(const TreeNode* root) {
        if (root == nullptr) return result;
        if (root->left == nullptr && root->right == nullptr && left) {
            result += root->val;
        }
        left = true;
        sumOfLeftLeaves(root->left);
        left = false;
        sumOfLeftLeaves(root->right);
        return result;
    }
    int result = 0;
    bool left = false;
};