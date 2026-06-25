// Last updated: 6/25/2026, 9:18:31 AM
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> umap;
        int max_len = 0, start = 0;
        for(int i=0; i<s.size(); i++){
            if(umap.find(s[i]) != umap.end()) start = max(start, umap[s[i]]+1);
            max_len = max(max_len, i-start+1);
            umap[s[i]] = i;
        }
        return max_len;
    }
};