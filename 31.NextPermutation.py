from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        wasModified = False
        n = len(nums)

        k = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break

        if k == -1:
            nums.reverse()
            return

        for i in range(n-1, k, -1):
            if nums[i] > nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
                break

        nums[k+1:] = reversed(nums[k+1:])