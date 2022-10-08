List = list


class SimpleSort:

    def insert_sort(nums):
        # 插入排序
        # 进阶： 希尔排序
        for i in range(1, len(nums)):
            x = nums[i]
            j = i
            # 反序逐个后移元素，确定插入位置
            while j > 0 and nums[j - 1] > x:
                nums[j] = nums[j - 1]
                j -= 1

            nums[j] = x

    def select_sort(nums):
        # 选择排序： 每次循环找到一个最小值
        # 进阶： 堆排序
        for i in range(len(nums) - 1):
            k = i
            for j in range(i, len(nums)):
                if nums[j] < nums[k]:
                    k = j

            nums[i], nums[k] = nums[k], nums[i]

    def bubble_sort(nums):
        # 冒泡排序(交换排序)
        # 快速排序
        for i in range(len(nums)):
            sorted_flag = True
            for j in range(1, len(nums) - 1):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    sorted_flag = False

            if sorted_flag:
                break


class QuickSort:

    def sortArray(self, nums: List[int]) -> List[int]:
        # quickSortArray(nums, 0, len(nums)-1)
        # quickSortArray1(nums, 0, len(nums) - 1)
        return nums

    def quickSortArray(nums, left, right):
        # 递归
        # 使用两个标记i，j将nums分成三段，直到i >= j
        # 小于pivot |   待分类  | 大于pivot
        #           i          j
        if left >= right:
            return

        i, j = left, right
        pivot = nums[i]
        while i < j:
            # 从右到左扫出小于pivot的记录，记录到左边i
            while i < j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1

            # 从左到右扫出大于pivot的记录，记录到右边j
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1

        nums[i] = pivot

        # quickSortArray(nums, left, i - 1)
        # quickSortArray(nums, i + 1, right)

    def quickSortArray1(nums, begin, end):
        # 使用两个标记i，j将nums分成三段
        # 小于pivot | 大于pivot | 待分类
        #           i          j
        # 使用一次循环即可将记录分成：小于pivot | 大于pivot
        # 递归调用，简单明了
        if begin >= end:
            return

        i = begin
        n = nums[i]
        for j in range(begin + 1, end + 1):
            if nums[j] < n:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[begin], nums[i] = nums[i], nums[begin]

        # quickSortArray1(nums, begin, i - 1)
        # quickSortArray1(nums, i + 1, end)


class HeapSort:
    """
    堆排序（小顶堆）
    """

    def heap_sort(nums):
        from heapq import heappop, heapify
        nums = heapify(nums)
        res = []
        while nums:
            res.apend(heappop(nums))
        return res


class ShellSort:
    """
    希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。
    希尔排序是非稳定排序算法。
    希尔排序是基于插入排序的以下两点性质而提出改进方法的：
    1. 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
    2. 插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位
    希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序
    待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序
    """

    def insert_sort(nums):
        # 插入排序
        for i in range(len(nums)):
            x = nums[i]
            j = i
            # 反序逐个后移元素，确定插入位置
            while j > 0 and nums[j - 1] > x:
                nums[j] = nums[j - 1]
                j -= 1

            nums[j] = x

    def shell_sort(nums):
        # 希尔排序
        length = len(nums)
        # 初始步长设置为总长度的一半
        step = length // 2
        while step >= 1:
            for i in range(length):
                x = nums[i]
                j = i
                # 在每一组里面进行直接插入排序
                while j >= step and nums[j - step] > x:
                    nums[j] = nums[j - step]
                    j -= step

                nums[j] = x
            # 减半步长
            step = step // 2


class MergeSort:
    '''
    归并排序，是创建在归并操作上的一种有效的排序算法。
    该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
    分割：递归地把当前序列平均分割成两半。
    集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
    '''

    def merge_sort(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        res = []
        while len(left) > 0 and len(right) > 0:
            # 左右两个数列第一个最小放前面
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))

        # 只有一个数列中还有值，直接添加
        res += left
        res += right
        return res


class BucketSort:
    '''
    桶排序(牺牲空间)
    桶排序的有效性需假定输入数据是由一个完全随机过程产生
    即要求桶排序的输入数据呈均匀分布，例如，输入数据随机均匀分布在区间[0, 1)。
    '''

    def bucket_sort(nums):
        min_num = min(nums)
        max_num = max(nums)
        # 桶的大小
        bucket_range = (max_num - min_num) / len(nums)
        # 桶数组
        count_list = [[] for i in range(len(nums) + 1)]
        # 向桶数组填数
        for i in nums:
            count_list[int((i - min_num) // bucket_range)].append(i)

        # 回填原数组
        nums.clear()
        for i in count_list:
            for j in sorted(i):
                nums.append(j)


class CountSort:
    """
    计数排序(牺牲空间)
    桶排序的有效性需假定输入数据是由一个完全随机过程产生
    所有数必须为整数
    """

    def count_sort(nums):
        # 找到最大最小值
        min_num = min(nums)
        max_num = max(nums)
        # 计数列表
        count_list = [0] * (max_num - min_num + 1)
        # 计数
        for i in nums:
            count_list[i - min_num] += 1

        nums.clear()
        # 填回
        for ind, i in enumerate(count_list):
            while i != 0:
                nums.append(ind + min_num)
                i -= 1
