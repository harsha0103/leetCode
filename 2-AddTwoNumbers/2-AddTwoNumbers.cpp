// Last updated: 6/25/2026, 9:18:33 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry=0;
        ListNode* result = l1;
        while(l1 != NULL and l2 != NULL){
            int val = l1->val + l2->val + carry;
            carry = val/10;
            l1->val = val%10;
            l1 = l1->next;
            l2 = l2->next;
        }
        if(l2 != NULL) {
            l1 = result;
            while(l1->next != NULL) l1 = l1->next;
            l1->next = l2; l1=l1->next;}
        while(l1 != NULL){
            int val = l1->val + carry;
            carry = val/10;
            l1->val = val%10;
            l1 = l1->next;
        }
        if(carry > 0){
            l1 = result;
            while(l1->next != NULL) l1 = l1->next;
            ListNode* temp = new ListNode();
            temp->val = carry;
            temp->next = NULL;
            l1->next = temp;
        }
        return result;
    }
};