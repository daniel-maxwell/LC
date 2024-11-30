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
        for (const TreeNode* node : nodes) {
            nodeSet.insert(node->val);
        }
        return dfs(root);
    }

    TreeNode* dfs(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        if (nodeSet.contains(root->val)) return root;

        TreeNode* left = dfs(root->left);
        TreeNode* right = dfs(root->right);

        if (left != nullptr && right != nullptr) {
            return root;
        } else if (left != nullptr) {
            return left;
        } else if (right != nullptr) {
            return right;
        }
        return nullptr;
    }

private:
    unordered_set<int> nodeSet{};
};