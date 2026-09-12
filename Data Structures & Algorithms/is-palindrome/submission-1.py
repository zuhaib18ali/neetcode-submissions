class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char.lower()
        p1 = 0
        p2 = len(new_str) - 1
        while p1 < p2:
            if new_str[p1] == new_str[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        
        return True