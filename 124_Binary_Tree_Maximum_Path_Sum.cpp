#include <stdio.h>
#include <string.h>
#include <malloc.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int path_max(int a, int b, int c) {
    if (b > a) a = b;
    if (c > a) a = c;
    return a;
}

void maxpath(struct TreeNode* root, int *ans) {
    int l = 0, r = 0;
    if (root->left != NULL) {
        maxpath(root->left, ans);
        l = root->left->val;
    }
    if (root->right != NULL) {
        maxpath(root->right, ans);
        r = root->right->val;
    }
    if (l + r + root->val > *ans) *ans = l + r + root->val;
    root->val += path_max(0, l, r);
    if (root->val > *ans) *ans = root->val;
}

int maxPathSum(struct TreeNode* root) {
    if (root == NULL) return 0;
    int ans = root->val;
    maxpath(root, &ans);
    return ans;
}
