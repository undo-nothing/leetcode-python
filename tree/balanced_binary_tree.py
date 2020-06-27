List = list


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BalancedBinaryTree:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def _helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = _helper(left, mid - 1)
            root.right = _helper(mid + 1, right)
            return root

        return _helper(0, len(nums) - 1)
