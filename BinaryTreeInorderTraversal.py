Given the root of a binary tree, return the inorder traversal of its nodes' values.
Example 1:
  
Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
  
left -> root -> right

################################################ Solution ##################################

# recursive solution as it is calling the function recursively
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
 ################################################ Solution ##################################

# this is an itertive appraoch to solve the problm
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []  # data strucvture to store the node value
        res = []
        if root is None:
            return []
        while root in not None or stack != []:
            while root in not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res = res.append(root.val)
            root = root.right
            
 

# for both the cases the time complexity and the space complexity is O(n) as we are traversing all the nodes once and storing into a stack/list
