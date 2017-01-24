#include <stdio.h>
#include <string.h>
#include <malloc.h>

int maximalRectangle(char** matrix, int matrixRowSize, int matrixColSize) {
    typedef struct _Node {
        int start, level;
    }Node;
    printf("%d %d\n", matrixRowSize, matrixColSize);
    Node *stack = (Node*)malloc(sizeof(Node)*matrixRowSize*matrixColSize);
    int *peak = (int*)malloc(sizeof(int)*matrixColSize);
    memset(peak, 0, sizeof(int)*matrixColSize);
    int ans = 0;
    printf("%d %d\n", matrixRowSize, matrixColSize);
    for (int i=0; i<matrixRowSize; i++) {
        for (int j=0; j<matrixColSize; j++) {
            printf("(%d,%d) %c\n", i,j, matrix[i][j]);
            if (matrix[i][j] == '1') {
                printf("!1\n");
                stack[j*matrixRowSize+peak[j]].level = i;
                if (j == 0 || matrix[i][j-1] == '0') stack[j*matrixRowSize+peak[j]].start = j;
                else stack[j*matrixRowSize+peak[j]].start = stack[(j-1)*matrixRowSize+(peak[j-1]-1)].start;
                peak[j] ++;
            } else {
                printf("!2\n");
                while (peak[j] != 0) {
                    peak[j] --;
                    int s = stack[j*matrixRowSize+peak[j]].start;
                    int l = stack[j*matrixRowSize+peak[j]].level;
                    if ((j-s+1)*(i-l)>ans) {ans = (j-s+1)*(i-l); printf("ans = %d\n", ans);}
                }
            }
        }
    }
    return ans;
}

int main() {
    char map[3][4] = {"0110","1111","1100"};
    printf("%d\n",maximalRectangle(map,3,4));
    return 0;
}
