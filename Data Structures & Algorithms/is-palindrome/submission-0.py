class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Basic approach - Reverse the string and check
        # O(n), O(n)
        # final_s = ""
        # for ch in s:
        #     if ch.isalnum():
        #         final_s += ch.lower()
        # return s == final_s[::-1]

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True