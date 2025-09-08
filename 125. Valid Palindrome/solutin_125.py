class Solution:
    """
    O(1) space complexity hence used ptrs.
    Good practice for me if I define my own isalnum() function
    """
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1

        while i<j:
            left_char, right_char = s[i].lower(), s[j].lower()

            if not left_char.isalnum():
                i+=1
                continue
            if not right_char.isalnum():
                j-=1
                continue
            
            if left_char!=right_char:
                return False
            i+=1
            j-=1
        
        return True

    def alphaNum(self, c):
        return ((ord('a') <= ord(c) <= ord('z')) or
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('0') <= ord(c) <= ord('9')))
            