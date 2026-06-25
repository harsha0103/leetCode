// Last updated: 6/25/2026, 9:14:43 AM
class Solution {
public:
    string ones(int n){
        if(n == 1) return "One ";
        if(n == 2) return "Two ";
        if(n == 3) return "Three ";
        if(n == 4) return "Four ";
        if(n == 5) return "Five ";
        if(n == 6) return "Six ";
        if(n == 7) return "Seven ";
        if(n == 8) return "Eight ";
        if(n == 9) return "Nine ";
        return "";
    }
    
    string tens(int n){
        if(n == 2) return "Twenty ";
        if(n == 3) return "Thirty ";
        if(n == 4) return "Forty ";
        if(n == 5) return "Fifty ";
        if(n == 6) return "Sixty ";
        if(n == 7) return "Seventy ";
        if(n == 8) return "Eighty ";
        if(n == 9) return "Ninety ";
        if(n == 10) return "Ten ";
        if(n == 11) return "Eleven ";
        if(n == 12) return "Twelve ";
        if(n == 13) return "Thirteen ";
        if(n == 14) return "Fourteen ";
        if(n == 15) return "Fifteen ";
        if(n == 16) return "Sixteen ";
        if(n == 17) return "Seventeen ";
        if(n == 18) return "Eighteen ";
        if(n == 19) return "Nineteen ";
        return "";
    }
    
    string numberToWords(int num) {
        if(num == 0) return "Zero";
        string result;
        int count = 0;
        while(num>0){
            int val = num%1000;
            string res;
            int one = val%10;
            int ten = (val/10)%10;
            if(ten == 1) {ten = val%100; one = 0;}
            int hun = val/100;
            if(hun>0) res += ones(hun) + "Hundred ";
            if(ten>0) res += tens(ten);
            if(ten<10) res += ones(one);
            if(val>0){
                if(count == 1) res += "Thousand ";
                if(count == 2) res += "Million ";
                if(count == 3) res += "Billion ";
            }
            result = res + result;
            num = num/1000;
            count++;
        }
        result.pop_back();
        return result;
    }
};