List = list


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LevelOrderSolution:
    '''
    二叉树的层次遍历
    给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
    in: [3,9,20,null,null,15,7]
        3
       / \
      9  20
        /  \
       15   7
    out:
    [
      [3],
      [9,20],
      [15,7]
    ]
    '''

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 循环
        res = []
        if not root:
            return res
        cur_nodes = [root]
        while cur_nodes:
            cur_nodes = []
            next_nodes = []
            for node in cur_nodes:
                cur_nodes.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            res.append(cur_nodes)
            cur_nodes = next_nodes
        return res

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        # 递归
        if not root:
            return []

        result = []

        def _travel(self, node, level):
            if not node:
                return

            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)

            _travel(node.left, level + 1)
            _travel(node.right, level + 1)

        _travel(root, 0)
        return result


class InOrderSolution:
    '''
    二叉树的中序遍历
    in: [1,null,2,3]
       1
        \
         2
        /
       3
    out: [1,3,2]
    '''

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack, node = [], [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            res.append(node.val)
            node = node.right

        return res

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []

        def _travel(root):
            if root is None:
                return

            _travel(root.left)
            res.append(root.val)
            _travel(root.right)

        _travel(root)
        return res


class PreOrderSolution:
    '''
    二叉树的前序遍历
    给定一个二叉树，返回它的 前序 遍历。

    示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3

    输出: [1,2,3]
    '''

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 循环
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        # 递归
        if not root:
            return []
        res = []
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res


class PostOrderSolution:
    '''
    给定一个二叉树，返回它的 后序 遍历。

    示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3

    输出: [3,2,1]
    '''

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 循环
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        # 递归
        if not root:
            return []
        res = []
        res += self.postorderTraversal1(root.left)
        res += self.postorderTraversal1(root.right)
        res.append(root.val)
        return res
