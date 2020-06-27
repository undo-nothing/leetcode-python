
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1  # (pos - 1) // 2
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


class HeapQuery:

    def __init__(self, elist):
        self._elems = list(elist)
        if elist:
            self._heapify()

    def _heapify(self):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        n = len(self._elems)
        # 初始的表看作是一课完全二叉树，从下标end//开始，后面的表都是书的叶子节点
        # 也就是说他们中的每个已是一个堆，只要_siftup前n // 2个元素即可
        for i in reversed(range(n // 2)):
            _siftup(self._elems, i)

    def heappush(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        self._elems.append(item)
        _siftdown(self._elems, 0, len(self._elems) - 1)

    def heappop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self._elems.pop()    # raises appropriate IndexError if heap is empty
        if self._elems:
            returnitem = self._elems[0]
            self._elems[0] = lastelt
            _siftup(self._elems, 0)
            return returnitem
        return lastelt
