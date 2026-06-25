// Last updated: 6/25/2026, 9:15:06 AM
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result;
        long long prod = 1; int flag = 0, no_flag = 0;
        for(auto x: nums){
            if(x==0) flag++;
            else {prod *= x; no_flag = 1;}
        }
        for(auto x: nums){
            if(no_flag==0 or flag>1) result.push_back(0);
            else if(flag == 1){
                if(x==0) result.push_back(prod);
                else result.push_back(0);
            }
            else result.push_back(prod/x);
        }
        return result;
    }
};