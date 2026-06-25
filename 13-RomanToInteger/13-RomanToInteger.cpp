// Last updated: 6/25/2026, 9:18:16 AM
class Solution {
public:
    int romanToInt(string s) {
        int num = 0;
        vector<char> roman{'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        for(int i=0; i<s.size(); i++){
            if(s[i] == 'M') num += 1000;
            else if(s[i] == 'D') num += 500;
            else if(s[i] == 'C'){
                if(i == s.size()-1) num += 100;
                else if(s[i+1] =='M') {num += 900; i++;}
                else if(s[i+1] =='D') {num += 400; i++;}
                else num += 100;
            }
            else if(s[i] == 'L') num += 50;
            else if(s[i] == 'X'){
                if(i == s.size()-1) num += 10;
                else if(s[i+1] =='C') {num += 90; i++;}
                else if(s[i+1] =='L') {num += 40; i++;}
                else num += 10;
            }
            else if(s[i] == 'V') num += 5;
            else if(s[i] == 'I'){
                if(i == s.size()-1) num += 1;
                else if(s[i+1] =='X') {num += 9; i++;}
                else if(s[i+1] =='V') {num += 4; i++;}
                else num += 1;
            }
        }
        return num;
    }
};