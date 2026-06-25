// Last updated: 6/25/2026, 9:17:45 AM
class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size()-1, max_index, max_val = INT_MIN, result = 0, max_left = height[0], max_right = height[height.size()-1];
        for(int i=0; i<height.size(); i++){
            if(max_val < height[i]){
                max_index = i;
                max_val = height[i];
            }
        }
        for(int i=0; i<max_index; i++){
            max_left = max(max_left, height[i]);
            result += max_left - height[i];
        }
        for(int i=height.size()-1; i>max_index; i--){
            max_right = max(max_right, height[i]);
            result += max_right - height[i];
        }
        return result;
    }
};