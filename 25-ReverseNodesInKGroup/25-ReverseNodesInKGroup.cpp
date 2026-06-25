// Last updated: 6/25/2026, 9:17:58 AM
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==1) return head;
        int length = 0; ListNode* trav = head;
        while(trav != NULL) {trav = trav->next; length++;}
        ListNode* post; trav=head; ListNode* prev=NULL;
        for(int i=0; i<length/k; i++){
            int t=k-1; ListNode* first = trav; ListNode* postnext;
            post = trav->next;
            while(t){
                postnext = post->next;
                post->next = trav;
                trav = post;
                post = postnext;
                t--;
            }
            if(prev==NULL) head = trav;
            else{prev->next = trav;}
            first->next = post;
            prev = first;
            trav = prev->next;
        }
        return head;
    }
};