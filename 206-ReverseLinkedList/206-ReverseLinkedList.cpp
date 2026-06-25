// Last updated: 6/25/2026, 9:15:32 AM
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
    ListNode* reverseList(ListNode* head) {
        if(head == NULL) return head;
        if(head->next == NULL) return head;
        ListNode* prev; ListNode* trav = head; ListNode* n = trav->next;
        while(n!= NULL){
            if(trav == head) trav->next = NULL;
            else trav->next = prev;
            prev = trav;
            trav = n;
            n = n->next;
        }
        trav->next = prev;
        return trav;
    }
};