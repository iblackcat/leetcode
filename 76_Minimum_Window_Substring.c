#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

char* minWindow(char* s, char* t) {
    typedef struct _Node{
        int num;
        struct _Node *next;
    } Node;
    struct Item{
        Node *st;
        Node *en;
        int num;
        int need;
    }item[256] = {0};
    int lens = strlen(s);
    int lent = strlen(t);
    printf("%d %d\n", lens, lent);

    int start=0, num=0, len=lens+1, ss=0, ee=0;
    int *now = (int*)malloc(lens*sizeof(int));
    memset(now, 0, sizeof(int)*lens);
    for (int i=0; i<lent; i++) item[t[i]].need++;
    for (int i=0; i<lens; i++) {
        int k = s[i];
        if (item[k].need == 0) continue;
        if (item[k].need == 1 && item[k].num == 1) {
            now[item[k].st->num] = 0;
            now[i] = 1;
            item[k].st->num = i;
        } else if (item[k].need > 0 && item[k].num == 0) {
            Node *p = (Node*)malloc(sizeof(Node));
            p->next = NULL;
            p->num = i;
            item[k].st = p;
            item[k].en = p;
            item[k].num++;
            now[i] = 1;
            num ++;
        } else if (item[k].need > 0 && item[k].num == item[k].need) {
            printf("--3\n");
            Node *p = item[k].st;
            if (p==NULL) printf("!!!\n");
            item[k].st = p->next;
            p->next = NULL;
            now[p->num] = 0;
            now[i] = 1;
            p->num = i;
            item[k].en->next = p;
            item[k].en = p;
        } else if (item[k].need > 0 && item[k].num < item[k].need) {
            Node *p = (Node*)malloc(sizeof(Node));
            p->next = NULL;
            p->num = i;
            now[i] = 1;
            item[k].en->next=p;
            item[k].en = p;
            item[k].num ++;
            num ++;
        }
        while (now[start] == 0) start++;
        printf("%d %d\n", start, i);
        for (int j=0; j<lens; j++) printf("%d", now[j]);
        printf("\n");
        if (num == lent && i-start+1 < len) {
            len = i-start+1;
            ss = start;
            ee = i;
        }
        printf("%d %d\n", ss, ee);
    }
    if (len == lens+1 && lent!=0) return "";
    else {
        printf("%d %d\n", ss,ee);
        s[ee+1] = '\0';
        return s+ss;
    }
}

int main() {
    char s[1024] = "kjaldkjfwefnkjekfbeffbckdjkvjdfvffdfcdsaafaa";
    char t[123] = "aabac";
    printf("%s\n", (char*)minWindow(s, t));
    return 0;
}
