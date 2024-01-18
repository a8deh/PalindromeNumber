class Solution:
  def isPalindrome(self, x: int) -> bool:
      x = str(x)
      n = x[::-1]
      if x == n:
        return True
      else:
        return False
print(Solution().isPalindrome(133)) # false
print(Solution().isPalindrome(333)) # true
