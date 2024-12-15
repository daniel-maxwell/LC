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
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        if (root->left == nullptr && root->right == nullptr) return vector<int> {root->val};
        getLeft(root->left);
        getRight(root->right);
        getLeaves(root);
        reverse(rightBoundary.begin(), rightBoundary.end());
        vector<int> result {root->val};
        result.insert(result.end(), leftBoundary.begin(), leftBoundary.end());
        result.insert(result.end(), leaves.begin(), leaves.end());
        result.insert(result.end(), rightBoundary.begin(), rightBoundary.end());
        return result;
    }

    void getLeft(TreeNode* root)  {
        if (root == nullptr || (root->left == nullptr && root->right == nullptr)) return;
        leftBoundary.push_back(root->val);
        if (root->left == nullptr) getLeft(root->right);
        else (getLeft(root->left));
    }

    void getRight(TreeNode* root)  {
        if (root == nullptr || (root->left == nullptr && root->right == nullptr)) return;
        rightBoundary.push_back(root->val);
        if (root->right == nullptr) getRight(root->left);
        else (getRight(root->right));
    }

    void getLeaves(TreeNode* root)  {
        if (root == nullptr) return;
        if (root->left == nullptr && root->right == nullptr) {
            leaves.push_back(root->val);
        } else {
            getLeaves(root->left);
            getLeaves(root->right);
        }
    }

private:
    vector<int> leftBoundary;
    vector<int> rightBoundary;
    vector<int> leaves;
};