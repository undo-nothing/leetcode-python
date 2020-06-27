List = list


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    从前序与中序遍历序列构造二叉树
    根据一棵树的前序遍历与中序遍历构造二叉树。

    注意:
    你可以假设树中没有重复的元素。

    例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7
    """

    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        index = 0
        for i in range(1, len(preorder)):
            node = stack[-1]
            # 表明该中序索引在左子树
            if(stack[-1].val != inorder[index]):
                node.left = TreeNode(preorder[i])
                stack.append(node.left)
            else:
                while len(stack) != 0 and stack[-1].val == inorder[index]:
                    # 表明该子树一表达完毕
                    node = stack.pop()
                    index += 1
                if index < len(inorder):
                    node.right = TreeNode(preorder[i])
                    stack.append(node.right)
        return root

    def buildTree1(self, preorder, inorder):
        pre_idx = 0
        idx_dict = {val: idx for idx, val in enumerate(inorder)}

        def _helper(left, right):
            nonlocal pre_idx

            if left == right:
                return None

            val = preorder[pre_idx]
            root = TreeNode(val)

            pre_idx += 1
            idx = idx_dict[val]
            root.left = _helper(left, idx)
            root.right = _helper(idx + 1, right)

            return root

        left, right = 0, len(preorder)
        return _helper(left, right)

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        val = preorder.pop(0)
        node = TreeNode(val)
        i = inorder.index(val)

        node.left = self.buildTree2(preorder[:i], inorder[:i])
        node.right = self.buildTree2(preorder[i:], inorder[i + 1:])
        return node


class Solution1:
    """
    从中序与后序遍历序列构造二叉树
    根据一棵树的中序遍历与后序遍历构造二叉树。

    注意:
    你可以假设树中没有重复的元素。

    例如，给出

    中序遍历 inorder = [9,3,15,20,7]
    后序遍历 postorder = [9,15,7,20,3]
    返回如下的二叉树：

        3
       / \
      9  20
        /  \
       15   7
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        last_idx = len(postorder) - 1
        idx_dict = {val: idx for idx, val in enumerate(inorder)}

        def _helper(left, right):
            nonlocal last_idx

            if left > right:
                return None

            val = postorder[last_idx]
            root = TreeNode(val)

            last_idx -= 1
            index = idx_dict[val]
            root.right = _helper(index + 1, right)
            root.left = _helper(left, index - 1)
            return root

        return _helper(0, len(inorder) - 1)

    def buildTree1(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        val = postorder.pop()
        i = inorder.index(val)

        node = TreeNode(val)
        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i + 1:], postorder[i:])
        return node


class Solution2:
    """
    根据前序和后序遍历构造二叉树
    返回与给定的前序和后序遍历匹配的任何二叉树。
    pre 和 post 遍历中的值是不同的正整数。

    示例：
    输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
    输出：[1,2,3,4,5,6,7]


    提示：
    1 <= pre.length == post.length <= 30
    pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
    每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
    """

    def constructFromPrePost(self, pre, post):
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        return root
