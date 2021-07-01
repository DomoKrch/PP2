class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0

        for i in range(len(nums)):
            if i + 1 != len(nums):
                j = i + 1
                while j < len(nums):
                    if nums[i] == nums[j]:
                        cnt = cnt + 1
                    j = j + 1

        return cnt
