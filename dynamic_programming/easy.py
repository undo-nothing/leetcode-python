List = list


class Solution:
    '''
    最大子序和
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例:

    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
    '''
    # k[n] = max(k[n-1], num[n])
    # dp[n] = max(dp[n-1], k[n])

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] = nums[i - 1] + nums[i]
            max_sum = max(max_sum, nums[i])

        return max_sum


class Solution1:
    '''
    爬楼梯
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

    注意：给定 n 是一个正整数。

    示例 1：

    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶
    示例 2：

    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶
    '''
    # dp[n] = dp[n-1] + dp[n-2]
    # 注意返回的是

    def climbStairs(self, n: int) -> int:
        i = 1
        j = 2
        for _ in range(3, n + 1):
            i, j = j, i + j

        return j if n > 1 else n


class Solution2:
    '''
    买卖股票的最佳时机
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

    如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

    注意你不能在买入股票前卖出股票。

    示例 1:

    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
         注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
    示例 2:

    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
    '''
    # 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
    # k[n] = v[n] - min(n-1)
    # dp[n] = max(dp[n-1], k[n])

    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_p = 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p


class Solution3:
    '''
    打家劫舍
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

    示例 1:

    输入: [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。
    示例 2:

    输入: [2,7,9,3,1]
    输出: 12
    解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
         偷窃到的最高金额 = 2 + 9 + 1 = 12 。
    '''
    # 打劫前i个房屋最大收益=max(打劫前i-2个房屋最大收益+第i家， 打劫前i-1个房屋最大收益)
    # dp[i] = max(dp[i-2]+nums[i], dp[i-1])

    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        curr_max = 0
        for value in nums:
            curr_max, prev_max = max(curr_max, prev_max + value), curr_max

        return curr_max


class Solution4:
    '''
    使用最小花费爬楼梯
    数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

    每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

    您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

    示例 1:

    输入: cost = [10, 15, 20]
    输出: 15
    解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
     示例 2:

    输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    输出: 6
    解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
    注意：

    cost 的长度将会在 [2, 1000]。
    每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
    '''
    # 注意到达楼顶可以有两种方式，从倒数第二台阶走两步或者倒数第一台阶走一步，故增加一个0体力的楼顶
    # dp[i] = max(dp[i-2], dp[i-1]) + cost[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_min = 0
        curr_min = 0
        cost.append(0)
        for value in cost:
            curr_min, prev_min = min(curr_min, prev_min) + value, curr_min

        return curr_min
