class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = "".join([char for char in s if char.isalnum()]).lower()
        return stripped_s == stripped_s[::-1]


        