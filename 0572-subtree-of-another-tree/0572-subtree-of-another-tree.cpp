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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        target = subRoot->val;
        targetLeft = subRoot->left != nullptr;
        targetRight = subRoot->right != nullptr;
        findSubRoot(root);
        for (TreeNode* psr : potentialSubRoots) {
            if (checkEquality(psr, subRoot)) return true;
        }
        return false;
    }

    void findSubRoot(TreeNode* root) {
        if (root == nullptr) return;
        if (root->val == target &&
           (root->left != nullptr) == targetLeft &&
           (root->right != nullptr) == targetRight
        ) potentialSubRoots.push_back(root);
        findSubRoot(root->left);
        findSubRoot(root->right);
    }

    bool checkEquality(TreeNode* root1, TreeNode* root2) {
        if (root1 == nullptr && root2 == nullptr) return true;
        if (root1 == nullptr || root2 == nullptr) return false;
        bool equal = root1->val == root2->val;
        return (
            equal && 
            checkEquality(root1->left, root2->left) && 
            checkEquality(root1->right, root2->right)
        );
    }

    int target;
    bool targetLeft;
    bool targetRight;

    vector<TreeNode*> potentialSubRoots;
};