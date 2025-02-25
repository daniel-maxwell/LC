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
    int countUnivalSubtrees(TreeNode* root) {
        if (root == nullptr) return 0;
        traverse(root);
        return total;
    }

    bool traverse(TreeNode* root) {
        if (!root) return true;  // by definition, null is trivially univalue

        bool leftUni = traverse(root->left);
        bool rightUni = traverse(root->right);

        if (!leftUni || !rightUni) {
            return false;
        }

        if (root->left && root->left->val != root->val) {
            return false;
        }
        if (root->right && root->right->val != root->val) {
            return false;
        }

        ++total;
        return true;
    }
    int total = 0;
};