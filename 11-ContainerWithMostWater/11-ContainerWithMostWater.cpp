// Last updated: 6/25/2026, 9:18:19 AM
class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0, j=height.size()-1, area = 0, breadth;
        while(i<j){
            breadth = min(height[i], height[j]);
            area = max(area, breadth * (j-i));
            if(breadth == height[i]) i++;
            else j--;
        }
        return area;
    }
};