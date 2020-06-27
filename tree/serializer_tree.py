class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return res
        cur_nodes = [root]
        while cur_nodes:
            cur_res = []
            child_nodes = []
            for node in cur_nodes:
                if node:
                    cur_res.append(node.val)
                    child_nodes.append(node.left)
                    child_nodes.append(node.right)
                else:
                    cur_res.append(None)
            res.extend(cur_res)
            cur_nodes = child_nodes

        while res[-1] is None:
            res.pop()

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        root = TreeNode(data[0])
        parents = [root]
        childs = []
        i = 1
        length = len(data)
        while i < length:

            if childs:
                parents = childs
                childs = []

            for parent in parents:
                if i < length and data[i] is not None:
                    node = TreeNode(data[i])
                    parent.left = node
                    childs.append(node)
                i += 1
                if i < length and data[i] is not None:
                    node = TreeNode(data[i])
                    parent.right = node
                    childs.append(node)
                i += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
