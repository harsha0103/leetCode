// Last updated: 6/25/2026, 9:18:04 AM
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == NULL) return list2;
        if(list2 == NULL) return list1;
        ListNode* trav; ListNode* trav2;
        if(list1->val > list2->val) {trav = list2; list2=list2->next;}
        else {trav = list1; list1=list1->next;}
        trav2 = trav;
        while(list2 != NULL and list1 != NULL){
            if(list1->val > list2->val) {trav->next = list2; trav=trav->next; list2=list2->next;}
            else {trav->next = list1; trav=trav->next; list1=list1->next;}
        }
        if(list2==NULL) trav->next = list1;
        else trav->next = list2;
        return trav2;
    }
};