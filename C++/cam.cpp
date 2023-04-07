/**  
 * Definition for a binary tree node.
 * Struct TreeNode{
 *      int val;
 *      TreeNode *left;
 *      TreeNode *right;
 * } 
*/
/**  
 * Definition for a binary tree node.
 * Struct TreeNode{
 *      int val;
 *      TreeNode *left;
 *      TreeNode *right;
 * } 
*/

class Solution {
public:
    int minCameraCover(TreeNode* root){
        int cameras = 0;
        if (root == nullptr) {
            return 0;
        }
        if (root -> left == nullptr && root -> right == nullptr){
            return 0;
        }
        if (root -> left != nullptr) {
            cameras += minCameraCover(root->left);
            if (root->left->val == 0){
                root->left->val = 1;
                root -> val = -1;
                cameras++;
                if (root->right != nullptr){
                    root->right->val = 1;
                }
            }
            if (root->left->val == -1){
                root->left->val = 1;
                root->val = 1;
            }
        }
        if (root -> right != nullptr) {  /** If not defined left side is not completing */
            cameras += minCameraCover(root->left);
            if (root->left->val == 0){
                root->left->val = 1;
                root -> val = -1;
                cameras++;
                if (root->right != nullptr){
                    root->right->val = 1;
                }
            }
    }
};