// Last updated: 6/25/2026, 9:16:18 AM
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    
    Node* copyRandomList(Node* head) {
        if(head==NULL) return head;
        Node* result = new Node(head->val);
        Node* res = result;
        Node* trav = head->next;
        while(trav != NULL){
            Node* temp = new Node(trav->val);
            res->next = temp;
            res = res->next;
            trav = trav->next;
        }
        trav = head; Node* trav2 = result;
        while(trav != NULL){
            Node* temp1 = head; Node* temp2 = result; Node* rand = trav->random;
            if(rand == NULL) {
                trav = trav->next;
                trav2 = trav2->next;
                continue;
            }
            while(temp1 != rand){
                temp1 = temp1->next;
                temp2 = temp2->next;
                if(temp1 == NULL) break;
            }
            trav2->random = temp2==NULL? NULL : temp2;
            trav = trav->next;
            trav2 = trav2->next;
        }
        return result;
    }
};