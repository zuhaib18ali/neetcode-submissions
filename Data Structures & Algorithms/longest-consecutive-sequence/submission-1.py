class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        current =1
        longest = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:

                current += 1
                longest = max(longest, current)
            else:
                current = 1
               
        return longest        