// Last updated: 6/25/2026, 9:14:10 AM
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> umap;
        for(auto x: s) umap[x]++;
        for(int i=0; i<s.size(); i++){
            if(umap[s[i]] == 1) return i;
        }
        return -1;
    }
};