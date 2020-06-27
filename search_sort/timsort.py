def insert_sort(nums):
    # 插入排序
    for i in range(1, len(nums)):
        x = nums[i]
        j = i
        # 反序逐个后移元素，确定插入位置
        while j > 0 and nums[j - 1] > x:
            nums[j] = nums[j - 1]
            j -= 1

        nums[j] = x


def merge(left, right):
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


def tim_sort(nums):
    length = len(nums)
    min_run = 5

    if not length:
        return nums

    run_stack = []

    count = length // min_run
    for i in range(count):
        # print(i * min_run, i * min_run + min_run)
        run_stack.append(nums[i * min_run:i * min_run + min_run])

    if nums[count * min_run:]:
        run_stack.append(nums[count * min_run:])

    for each in run_stack:
        insert_sort(each)

    new_stack = []
    while True:
        if len(run_stack) > 1:
            new_stack.append(merge(run_stack.pop(), run_stack.pop()))
            continue
        else:
            if len(run_stack) == 1:
                if len(new_stack) == 0:
                    break
                new_stack.append(run_stack.pop())
            run_stack = new_stack
            new_stack = []

    return run_stack[0]


if __name__ == '__main__':
    # tim sort: 待优化， 思路参考：https://www.cnblogs.com/brucecloud/p/6085703.html
    arr = [45, 2.1, 3, 67, 21, 90, 20, 13, 45, 23, 12, 34, 56, 78, 90, 0, 1, 2, 3, 1, 2, 9, 7, 8, 4, 6]
    arr = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
    arr = [5, 1, 1, 2, 0, 0]
    arr = tim_sort(arr)
    print(arr)
