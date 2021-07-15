import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.arr1 = [nums[i] for i in range(len(nums))]
        self.arr2 = [nums[i] for i in range(len(nums))]  # 不能直接赋值

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr1 = [self.arr2[i] for i in range(len(self.arr2))]
        return self.arr1

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.arr1)):
            ind = random.randrange(i, len(self.arr1))
            self.arr1[i], self.arr1[ind] = self.arr1[ind], self.arr1[i]
        return self.arr1