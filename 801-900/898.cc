// Author: Huahua

/*
Solutio 1: DP

dp[i][j] := A[i] | A[i + 1] | … | A[j]
dp[i][j] = dp[i][j – 1] | A[j]
ans = len(set(dp))

*/

// Time complexity: O(n^2)
// Space complexity: O(n^2)
// Running time: TLE (73/83 passed).
class Solution {
public:
  int subarrayBitwiseORs(vector<int>& A) {
    int n = A.size();
    vector<vector<int>> dp(n, vector<int>(n));
    unordered_set<int> ans(begin(A), end(A));
    for (int l = 1; l <= n; ++l)
      for (int i = 0; i <= n - l; ++i) {        
        int j = i + l - 1;
        if (l == 1) {
          dp[i][j] = A[i];
          continue;
        }
        dp[i][j] = dp[i][j - 1] | A[j];
        ans.insert(dp[i][j]);
      }
    return ans.size();
  }
};

// O(n) Space
// Running time: TLE (75/83 passed)
class Solution {
public:
  int subarrayBitwiseORs(vector<int>& A) {
    int n = A.size();
    vector<int> dp(A);
    unordered_set<int> ans(begin(A), end(A));
    for (int l = 2; l <= n; ++l)
      for (int i = 0; i <= n - l; ++i)        
        ans.insert(dp[i] |= A[i + l - 1]);
    return ans.size();
  }
};

/* 
Solution 2: DP optimized
dp[i] := {A[i], A[i] | A[i – 1], A[i] | A[i – 1] | A[i – 2], … , A[i] | A[i – 1] | … | A[0]}
bitwise ors of all subarrays end with A[i].
|dp[i]| <= 32
Proof: all the elements (in the order of above sequence) in dp[i] are monotonically increasing by 
flipping 0 bits to 1 from A[i]. There are at most 32 0s in A[i]. Thus the size of the set is <= 32.
证明： dp[i] = {A[i], A[i] | A[i – 1], A[i] | A[i – 1] | A[i – 2], … , A[i] | A[i – 1] | … | A[0]}
这个序列单调递增，通过把A[i]中的0变成1。A[i]最多有32个0。所以这个集合的大小 <= 32。
e.g. 举例：Worst Case 最坏情况 A = [8, 4, 2, 1, 0] A[i] = 2^(n-i)。
A[5] = 0，dp[5] = {0, 0 | 1, 0 | 1 | 2, 0 | 1 | 2 | 4, 0 | 1 | 2 | 4 | 8} = {0, 1, 3, 7, 15}.

Time complexity: O(n*log(max(A))) < O(32n)
Space complexity: O(n*log(max(A)) < O(32n)
*/

// Running time: 456 ms
class Solution {
public:
  int subarrayBitwiseORs(vector<int>& A) {
    unordered_set<int> ans;
    unordered_set<int> cur;
    unordered_set<int> nxt;
    for (int a : A) {
      nxt.clear();
      nxt.insert({a});
      for (int b : cur) {
        nxt.insert(a | b);
      }
      cur.swap(nxt);
      ans.insert(begin(cur), end(cur));
    }
    return ans.size();
  }
};
