// Last updated: 6/25/2026, 9:12:17 AM
class Solution {
public:
    int fib(int n) {
        // DP
        if(n==0) return 0;
        if(n==1) return 1;
        int prev1=1, prev2=0, result;
        for(int i=2; i<=n; i++){
            result = prev1+prev2;
            prev2=prev1;
            prev1=result;
        }
        return result;
    }
};