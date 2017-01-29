#include <stdio.h>
#include <string.h>
#include <malloc.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void recoverl(struct TreeNode* root, struct TreeNode* l_r, struct TreeNode* r_r, struct TreeNode** l) {
    if (root == NULL) return;
    recoverl(root->right, root, r_r, l);
    if (r_r != NULL && root->val > r_r->val) *l = root;
    if (root->left != NULL && root->right != NULL && root->left->val > root->right->val) *l = root->left;
    if (l_r != NULL && root->val < l_r->val) *l = l_r;
    recoverl(root->left, l_r, root, l);
}

void recoverr(struct TreeNode* root, struct TreeNode* l_r, struct TreeNode* r_r, struct TreeNode** r) {
    if (root == NULL) return;
    recoverr(root->left, l_r, root, r);
    if (l_r != NULL && root->val < l_r->val) *r = root;
    if (root->left != NULL && root->right != NULL && root->left->val > root->right->val) *r = root->right;
    if (r_r != NULL && root->val > r_r->val) *r = r_r;
    recoverr(root->right, root, r_r, r);
}

void recoverTree(struct TreeNode* root) {
    struct TreeNode *l = NULL, *r = NULL;
    recoverl(root, NULL, NULL, &l);
    recoverr(root, NULL, NULL, &r);
    if (l != NULL && r != NULL) {
        int tmp = l->val;
        l->val = r->val;
        r->val = tmp;
    }
}

int main() {


}
