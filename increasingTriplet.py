class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for index in range(len(nums) - 2):
            for index1 in range(index, len(nums) - 1):
                if nums[index1] > nums[index]:
                    for index2 in range(index1, len(nums)):
                        if nums[index2] > nums[index1]:
                            return True
        return False

    def increasingTripletFast(self, nums):
        begin = 0
        mid = None
        for index in range(1, len(nums)):
            if mid is None:
                if nums[index] > nums[begin]:
                    mid = index
                else:
                    begin = index
            elif nums[index] > nums[mid]:
                return True
            elif nums[index] > nums[begin]:
                mid = index
            else:
                begin = index
        return False


solution = Solution()
print(solution.increasingTriplet([20, 100, 10, 12, 5, 11, 24]))
print(solution.increasingTripletFast([20, 100, 10, 12, 5, 11, 24]))
