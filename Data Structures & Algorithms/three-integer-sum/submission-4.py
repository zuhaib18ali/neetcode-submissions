class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        final=[]
        for i in range(len(nums)):
            num = nums[i]
            need1 = 0 - num
            p1= i + 1
            p2= len(nums) - 1
            while p1 < p2:
                current = nums[p1] + nums[p2]
                if current == need1:
                    finale = [num,nums[p1],nums[p2]]
                    final.append(finale)
                    p1 += 1
                    p2 -= 1
                elif current < need1:
                    p1 += 1
                else:
                    p2 -= 1
        final = [tuple(x) for x in final]
        final = list(set(final))
        ans = [list(x) for x in final] 
        return ans