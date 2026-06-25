// Last updated: 6/25/2026, 9:18:05 AM
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int min_val = INT_MAX;
        sort(nums.begin(), nums.end());
        for(int i=0; i<nums.size()-2; i++){
            int target1 = target - nums[i],low = i+1, high = nums.size()-1;
            while(low<high){
                if(abs(min_val) > abs(target1 - nums[low] - nums[high])){
                    min_val = target1 - nums[low] - nums[high];
                }
                if(nums[low] + nums[high] < target1) low++;
                else if(nums[low] + nums[high] > target1) high--;
                else break;
            }
        }
        return target - min_val;
    }
};