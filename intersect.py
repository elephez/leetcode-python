class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        for num1 in nums1:
            if num1 in nums2:
                nums2.remove(num1)
                ret.append(num1)
        return ret


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    ret = solution.intersect(nums1, [2, 2])
    print(ret)
