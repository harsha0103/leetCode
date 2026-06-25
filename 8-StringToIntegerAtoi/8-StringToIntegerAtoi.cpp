// Last updated: 6/25/2026, 9:18:22 AM
class Solution {
public:
    int myAtoi(string s) {
        bool int_flag = false;
        long long result = 0;
        int sign = 1;
        for(auto x: s){
            if(x==' '){
                if(int_flag) break;
                continue;
            }
            if(x=='-' and !int_flag) {sign = -1; int_flag = true;}
            else if(x=='+' and !int_flag) {sign = 1; int_flag = true;}
            else if(x-'0'>-1 and x-'0'<10){
                int_flag = true;
                result = result * 10 + (x-'0');
            }
            else{
                if(int_flag) break;
                if(!int_flag and x!=' ') break;
            }
            if(sign * result > INT_MAX) return INT_MAX;
            if(sign * result < INT_MIN) return INT_MIN;
        }
        result *= sign;
        return result;
    }
};