class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in nums:
            sum += i
        if sum-nums[0] == 0:
            return 0
        i=0
        leftSum = 0
        while i!= len(nums):
            sum = sum-nums[i]
            if leftSum == sum:
                return i
            else:
                leftSum += nums[i]
            i += 1
        return -1

