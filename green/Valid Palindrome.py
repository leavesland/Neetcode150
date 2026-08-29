class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0, len(s)-1
        for i in range (len(s)-1):
            if s[left].isalnum()==False:
                left+=1
            elif s[right].isalnum()==False:
                right-=1
            elif s[left].lower()!=s[right].lower():
                return False
            else:
                left+=1
                right = right - 1
        return True