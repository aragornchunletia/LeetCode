
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string using preorder traversal.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def helper(node):
            if not node:
                res.append("#")  # Use '#' to represent null nodes
                return
            res.append(str(node.val))  # Store the current node value
            helper(node.left)
            helper(node.right)

        helper(root)
        return ",".join(res)  # Convert list to string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(","))  # Use an iterator for efficient processing

        def buildTree():
            val = next(values)
            if val == "#":
                return None  # Return None for null markers
            node = TreeNode(int(val))  # Create a new TreeNode
            node.left = buildTree()  # Recursively build left subtree
            node.right = buildTree()  # Recursively build right subtree
            return node

        return buildTree()
