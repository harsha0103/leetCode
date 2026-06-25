// Last updated: 6/25/2026, 9:15:57 AM
class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<int> v1, v2; int c1 = 0, c2 = 0;
        for(int i=0; i<version1.size(); i++) if(version1[i] == '.') c1++;
        for(int i=0; i<version2.size(); i++) if(version2[i] == '.') c2++;
        int i=0, j=0;
        while(c1 != -1 and c2 != -1){
            int sum1 = 0, sum2 = 0;
            while(version1[i] != '.' and i<version1.size()) {sum1 = 10*sum1 + int (version1[i]-'0'); i++;}
            while(version2[j] != '.' and j<version2.size()) {sum2 = 10*sum2 + int (version2[j]-'0'); j++;}
            if(sum1 < sum2) return -1;
            else if(sum1>sum2) return 1;
            c1--; c2--; i++; j++;
        }
        while(j<version2.size()){
            int sum1 = 0;
            while(version2[j] != '.' and j<version2.size()) {sum1 = 10*sum1 + int (version2[j]-'0'); j++;}
            if(sum1 > 0) return -1; j++;
        } cout<<1;
        while(i<version1.size()){
            int sum1 = 0;
            while(version1[i] != '.' and i<version1.size()) {sum1 = 10*sum1 + int (version1[i]-'0'); i++;}
            if(sum1 > 0) return 1; i++;
        }
        return 0;
    }
};