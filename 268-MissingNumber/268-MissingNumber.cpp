// Last updated: 6/25/2026, 9:14:49 AM
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int number = 0;
        for(int i=0; i<nums.size(); i++) number += i-nums[i];
        return number+nums.size();
    }
};