class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 前缀乘以后缀即可
        l = [1]
        for index in range(len(nums)):
            l.insert(index + 1, l[index] * nums[index])
        ridx = len(nums) - 1
        r = 1
        while ridx >= 0:
            l[ridx] = l[ridx] * r
            r *= nums[ridx]
            ridx -= 1
        l.pop()
        return l


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4, 5]))
