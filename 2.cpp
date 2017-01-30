#include <iostream>
#include <cstdio>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode *p = NULL, *last = NULL, *ans = NULL;
    int n1, n2, c = 0;
    while (l1 != NULL || l2 != NULL || c != 0) {
        n1 = l1 != NULL ? l1->val : 0;
        n2 = l2 != NULL ? l2->val : 0;
        c = n1 + n2 + c;
        p = new ListNode(c % 10);
        c /= 10;
        if (last != NULL) last->next = p;
        else ans = p;
        last = p;
        l1 = l1 != NULL ? l1->next : NULL;
        l2 = l2 != NULL ? l2->next : NULL;
    }
    return ans;
}

int main() {
    freopen("2.txt", "r", stdin);
    int n, a, b;
    scanf("%d", &n);
    ListNode *l1 = NULL, *l2 = NULL, *last1 = NULL, *last2 = NULL;
    for (int i = 0; i < n; i ++) {
        scanf("%d %d", &a, &b);
        l1 = new ListNode(a);
        l2 = new ListNode(b);
        l1->next = last1;
        l2->next = last2;
        last1 = l1;
        last2 = l2;
    }
    last1 = addTwoNumbers(l1, l2);
    while (last1 != NULL) {
        printf("%d->", last1->val);
        last1 = last1->next;
    }
    printf("\n");
    return 0;
}
