class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        t_area = 0
        while left < right:

            width = right - left
            area = width * min(heights[left], heights[right])

            if t_area <= area:
                t_area = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return t_area