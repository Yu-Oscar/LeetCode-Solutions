class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(char for char in s if char.isalnum()).lower()
        return string == string[::-1]