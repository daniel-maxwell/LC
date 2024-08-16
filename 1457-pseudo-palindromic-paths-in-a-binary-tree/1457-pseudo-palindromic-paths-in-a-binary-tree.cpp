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
  int currNumOdds = 0;
  int result = 0;
  map<int, int> counts;
  int pseudoPalindromicPaths(TreeNode *root) {
    if (!root) {
      return result;
    }
    if (counts.contains(root->val)) {
        counts[root->val]++;
    } else {
        counts[root->val] = 1;
    }
    if (counts[root->val] % 2 == 1) {
        currNumOdds++;
    } else {
        currNumOdds--;
    }

    if (!root->left && !root->right) {
      if (currNumOdds <= 1) {
        result++;
      }
    }

    pseudoPalindromicPaths(root->left);
    pseudoPalindromicPaths(root->right);

    counts[root->val]--;
    if (counts[root->val] % 2 == 0) {
        currNumOdds--;
    } else {
        currNumOdds++;
    }

    return result;
  }
};
