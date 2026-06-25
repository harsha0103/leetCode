// Last updated: 6/25/2026, 9:17:33 AM
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> umap;
        if(strs.size()==0) return result;
        for(int i=0; i<strs.size(); i++){
            string s = strs[i];
            sort(s.begin(), s.end());
            umap[s].push_back(strs[i]);
        }
        for(auto i: umap){
            result.push_back(i.second);
        }
        return result;
    }
};