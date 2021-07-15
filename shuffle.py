import copy
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.arranges = []
        self.dfs(nums, [])

    def dfs(self, nums, curr):
        if len(nums) == 0:
            cp = copy.copy(curr)
            self.arranges.append(cp)
        for index in range(len(nums)):
            num = nums[index]
            curr.append(num)
            del nums[index]
            self.dfs(nums, curr)
            curr.remove(num)
            nums.insert(index, num)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return self.arranges[random.randint(0, len(self.arranges) - 1)]


if __name__ == '__main__':
    solution = Solution([1, 2, 3])
    print(solution.arranges)
    print(solution.shuffle())
