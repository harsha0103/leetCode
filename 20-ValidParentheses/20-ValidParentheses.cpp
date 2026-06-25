// Last updated: 6/25/2026, 9:18:06 AM
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(int i=0; i<s.size(); i++){
            if(st.empty()) {st.push(s[i]); continue;}
            char c = st.top();
            cout<<st.top();
            if((s[i] - c)<3 and (s[i] - c)>0) st.pop(); 
            else st.push(s[i]);
        }
        if(st.empty()) return true;
        return false;
    }
};