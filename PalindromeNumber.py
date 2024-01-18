class Solution:
  def isPalindrome(self, x: int) -> bool:
      x = str(x) # 133 = 133
      n = x[::-1] # 331 = 133
      if x == n:
        return True
      else:
        return False
print(Solution().isPalindrome(133)) # false
print(Solution().isPalindrome(333)) # true
