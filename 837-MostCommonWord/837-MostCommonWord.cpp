// Last updated: 6/25/2026, 9:12:33 AM
class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        string t = "";
        unordered_map<string, int> umap, counts;
        for(int i=0; i<banned.size(); i++) umap[banned[i]]++;
        for(int i=0; i<paragraph.size(); i++){
            char x=paragraph[i];
            if(x>='A' and x<='Z') x += 'a'-'A';
            if(x!=' ' and x!='!' and x!='?' and x!='\'' and x!=',' and x!=';' and x!='.' and x!='"') t = t+x;
            else{
                if(umap.find(t) == umap.end() and t!=""){
                    counts[t]++;
                }
                t="";
            }
        }
        if(t!="") if(umap.find(t) == umap.end()) counts[t]++;
        int max_val=INT_MIN;
        for(auto x: counts){
            if(max_val < x.second){
                max_val = x.second;
                t = x.first;
            }
        }
        return t;
    }
};