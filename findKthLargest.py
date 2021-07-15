class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.odd = False
        self.mid = -1
        self.array = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.array.append(num)
        self.odd = bool(1 - self.odd)
        if self.odd:
            self.mid += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.odd:
            return self.array[self.mid]
        else:
            return (self.array[self.mid] + self.array[self.mid + 1]) / float(2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
