// Last updated: 6/25/2026, 9:18:10 AM
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for(int i=0; i<nums.size()-2; i++){
            if(i>0 && nums[i] == nums[i-1]) continue;
            int target = -nums[i], j=i+1, k=nums.size()-1;
            while(j<k){
                if(nums[j]+nums[k] == target) {
                    result.push_back({nums[i], nums[j], nums[k]});
                    while(j<k && nums[j] == nums[j+1]) j++;
                    while(j<k && nums[k] == nums[k-1]) k--;
                    j++; k--;
                }
                else if(nums[j]+nums[k] > target) k--;
                else j++;
            }
        }
        return result;
    }
};