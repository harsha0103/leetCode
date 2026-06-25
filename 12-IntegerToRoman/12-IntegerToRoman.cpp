// Last updated: 6/25/2026, 9:18:18 AM
class Solution {
public:
    string intToRoman(int num) {
        string s; int x=num;
        while(x>=1000){ s.push_back('M'); x -= 1000;}
        if(x>=900) {s.push_back('C'); s.push_back('M'); x-=900;}
        if(x>=500) {s.push_back('D'); x-=500;}
        if(x>=400) {s.push_back('C'); s.push_back('D'); x-=400;}
        while(x>=100) {s.push_back('C'); x-=100;}
        if(x>=90) {s.push_back('X'); s.push_back('C'); x-=90;}
        if(x>=50) {s.push_back('L'); x-=50;}
        if(x>=40) {s.push_back('X'); s.push_back('L');; x-=40;}
        while(x>=10) {s.push_back('X'); x-=10;}
        if(x>=9) {s.push_back('I'); s.push_back('X'); x-=9;}
        if(x>=5) {s.push_back('V'); x-=5;}
        if(x>=4) {s.push_back('I'); s.push_back('V'); x-=4;}
        while(x>=1) {s.push_back('I'); x-=1;}
        
        return s;
    }
};