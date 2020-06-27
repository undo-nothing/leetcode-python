List = list


class Solution:
    '''
    最小路径和
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

    说明：每次只能向下或者向右移动一步。

    示例:

    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。
    '''
    # dp[m, n] = min(dp[m-1, n], dp[m, n-1]) + grid[m][n]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)

        # 构造第一行查询表
        dp = grid[0]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + dp[i]
        dp.append(dp[0])

        for i in range(1, n):
            for j in range(m):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
            dp[-1] = dp[0]
        return dp[m - 1]


class Solution1:
    '''
    不同路径
    一个机器人位于一个 m x n 网格的左上角。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（。

    问总共有多少条不同的路径？

    示例 1:

    输入: m = 3, n = 2
    输出: 3
    解释:
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向右 -> 向下
    2. 向右 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向右
    示例 2:

    输入: m = 7, n = 3
    输出: 28
    '''
    # dp[m, 1], dp[1, m] = 1, 1
    # dp[m, n] = dp[m-1, n] + dp[m, n-1]

    def uniquePaths(self, m: int, n: int) -> int:
        # 构造初始查询列表，当n=1时 初始值路径都为1
        dp = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] = dp[j - 1] + dp[j]

        return dp[m - 1]


class Solution2:
    '''
    最佳买卖股票时机含冷冻期
    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    示例:

    输入: [1,2,3,0,2]
    输出: 3
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
    '''
    '''
    buy[i] means before day i what is the maxProfit for any sequence end with buy.

    sell[i] means before day i what is the maxProfit for any sequence end with sell.

    rest[i] means before day i what is the maxProfit for any sequence end with rest.

    buy[i]  = max(rest[i-1]-price, buy[i-1])
    sell[i] = max(buy[i-1]+price, sell[i-1])
    rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
    '''

    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell


class Solution3:
    '''
    最长上升子序列
    给定一个无序的整数数组，找到其中最长上升子序列的长度。

    示例:

    输入: [10,9,2,5,3,7,101,18]
    输出: 4
    解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
    说明:

    可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
    你算法的时间复杂度应该为 O(n2) 。
    '''

    '''
    [4, 5, 6, 3]
    len = 1   :      [4]          => tails = [4]
    len = 2   :      [4, 5]       => tails = [4, 5]
    len = 3   :      [4, 5, 6]    => tails = [4, 5, 6]
    len = 4   :      [4, 5, 6, 3] => tails = [3, 5, 6]

    (1) if x is larger than all tails, append it, increase the size by 1
    (2) if tails[i-1] < x <= tails[i], update tails[i]
    '''

    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            # 二分法找到需要更新的位置
            left, right = 0, size
            while left < right:
                m = (left + right) // 2
                if tails[m] < x:
                    left = m + 1
                else:
                    right = m
            tails[left] = x
            size = max(left + 1, size)
        return size


class Solution4:

    '''
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

    示例 1:

    输入: coins = [1, 2, 5], amount = 11
    输出: 3
    解释: 11 = 5 + 5 + 1
    示例 2:

    输入: coins = [2], amount = 3
    输出: -1
    说明:
    你可以认为每种硬币的数量是无限的。
    '''
    # dp[n] = min(dp[n-i1], dp[n-i2], ..., dp[ik]) + 1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1


class Solution5:

    '''
    打家劫舍 II
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
    同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

    示例 1:

    输入: [2,3,2]
    输出: 3
    解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
    示例 2:

    输入: [1,2,3,1]
    输出: 4
    解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
         偷窃到的最高金额 = 1 + 3 = 4 。
    '''
    # dp[i] = max(dp[i-2]+nums[i], dp[i-1])

    def rob(self, nums: List[int]) -> int:
        def sub_rob(nums):
            #  dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            last = 0
            now = 0
            for value in nums:
                now, last = max(now, last + value), now

            return now
        if len(nums) == 1:
            return nums[0]
        return max(sub_rob(nums[0:-1]), sub_rob(nums[1:]))
