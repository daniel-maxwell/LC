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
    TreeNode* lowestCommonAncestor(TreeNode* root, vector<TreeNode*> &nodes) {
        targetSet = unordered_set<TreeNode*>(nodes.begin(), nodes.end());
        return dfs(root);
    }

    TreeNode* dfs(TreeNode* root) {
        if (root == nullptr) return nullptr;

        TreeNode* left = dfs(root->left);
        TreeNode* right = dfs(root->right);

        if (left != nullptr && right != nullptr) {
            return root;
        } else if (left != nullptr || right != nullptr) {
            if (targetSet.contains(root)) {
                return root;
            } else {
                return left != nullptr ? left : right;
            }
        } else {
            return targetSet.contains(root) ? root : nullptr;
        }
    }

    unordered_set<TreeNode*> targetSet;
    TreeNode* result;
};