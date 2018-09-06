// Author: Huahua
// Running time: 434 ms
class Solution {
  public int subarrayBitwiseORs(int[] A) {
    Set<Integer> ans = new HashSet<>();
    Set<Integer> cur = new HashSet<>();
    for (int a : A) {
      Set<Integer> nxt = new HashSet<>();
      nxt.add(a);
      for (int b : cur)
        nxt.add(a | b);
      ans.addAll(nxt);
      cur = nxt;
    }
    return ans.size();
  }
}
