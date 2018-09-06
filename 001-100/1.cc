// Author: Huahua

// Solution 1: Brute Force
// Time complexity: O(n^2)
// Space complexity: O(1)
// Runtime: 166 ms
class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); ++i) {
      for (int j = i + 1;j < nums.size(); ++j) {
        int sum = nums[i] + nums[j];
        if (sum == target) {
          return {i, j};
        }
      }
    }
    return {};
  }
};

// Solution 2: HashTable
// Runtime: 6 ms
class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> indies;
    for (int i = 0; i < nums.size(); ++i)
      indies[nums[i]] = i;
    
    for (int i = 0; i < nums.size(); ++i) {
      int left = target - nums[i];
      if (indies.count(left) && indies[left] != i) {
          return {i, indies[left]};
      }
    }
    return {};
  }
};
