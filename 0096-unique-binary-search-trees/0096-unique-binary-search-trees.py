class Solution:
    """
    This is a combinatorics problem based on the concept of Catalan numbers.  
    The number of unique BSTs that can be formed with `n` nodes is determined by:  
    - Choosing a root node `i` (1 to n).  
    - The left subtree consists of `i-1` nodes.  
    - The right subtree consists of `n-i` nodes.  
    - The total number of BSTs is the product of the number of ways to form left and right subtrees,  
      summed over all possible root nodes.
    """
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)

        # Base cases: There's one way to form a BST with 0 or 1 node.
        dp[0], dp[1] = 1, 1

        for node in range(2, n + 1):
            total = 0
            for i in range(1, node + 1):  # Iterate over possible root nodes
                left = i - 1   # Nodes in the left subtree
                right = node - i  # Nodes in the right subtree
                total += dp[left] * dp[right]  # Multiply ways to form left and right subtrees
            dp[node] = total  # Store result for `node` nodes

        return dp[n]
