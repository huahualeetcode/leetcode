# Author: Huahua
# Running time: 812 ms
class Solution:
  def subarrayBitwiseORs(self, A):
    cur = set()
    ans = set()
    for a in A:
      cur = {a | b for b in cur} | {a}
      ans |= cur      
    return len(ans)
