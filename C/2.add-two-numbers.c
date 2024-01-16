#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
#include <stdint.h>
/*
 * @lc app=leetcode.cn id=2 lang=c
 *
 * [2] Add Two Numbers
 */

// @lc code=start

//Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* dummySum = malloc(sizeof(struct ListNode));
    struct ListNode* sum = malloc(sizeof(struct ListNode));
    struct ListNode* p = l1;
    struct ListNode* q = l2;
    
    int x = 0;
    dummySum->next = sum;

    while ( sum ){
        if (p != NULL){
            x += p->val;
            p = p->next;
        }else {
            x += 0;
        }
        if (q != NULL){
            x += q->val;
            q = q->next;
        }else {
            x += 0;
        }

        sum->val = x%10;
        x /= 10;
        if (p || q || x!=0){
            sum->next = malloc(sizeof(struct ListNode));
        }else {
            sum->next = NULL;
        }
        sum = sum->next;
    }

    return dummySum->next;
}
// @lc code=end

