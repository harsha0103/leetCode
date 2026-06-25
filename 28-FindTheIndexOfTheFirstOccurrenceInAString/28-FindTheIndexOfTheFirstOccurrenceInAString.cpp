// Last updated: 6/25/2026, 9:17:54 AM
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(haystack.size()<needle.size()) return -1;
        for(int i=0; i<haystack.size()-needle.size()+1; i++){
            if(haystack[i] == needle[0]){
                for(int j=0; j<needle.size(); j++){
                    if(needle[j] != haystack[i+j]) break;
                    if(j==needle.size()-1) return i;
                }
            }
        }
        return -1;
    }
};