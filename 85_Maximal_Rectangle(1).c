int maximalRectangle(char** matrix, int matrixRowSize, int matrixColSize) {
    int *heights = (int*)malloc(sizeof(int)*matrixColSize);
    int *stack = (int*)malloc(sizeof(int)*matrixColSize);
    memset(heights, 0, sizeof(int)*matrixColSize);
    int peak = 0, ans = 0, l;
    for (int i=0; i<matrixRowSize; i++) {
        for (int j=0; j<matrixColSize; j++) {
            if (matrix[i][j] == '0') heights[j] = 0;
            else heights[j] ++;
        }
        peak = 0;
        for (int k=0; k<matrixColSize; k++) {
            //printf("%d:", heights[k]);
            if (peak > 0) {
                while (peak>0 && heights[stack[peak-1]]>heights[k]) {
                    peak--;
                    l = k;
                    if (peak > 0) l = k - stack[peak-1] - 1;
                    if (heights[stack[peak]]*l > ans) ans = heights[stack[peak]]*l;
                    //printf("%d(%d,%d) ", heights[stack[peak]]*l, l, stack[peak]);
                    if (peak == 0) break;
                }
            }
            stack[peak++] = k;
            //printf("\n");
        }
        while (peak>0) {
            peak--;
            l = matrixColSize;
            if (peak > 0) l = matrixColSize - stack[peak-1] - 1;
            if (heights[stack[peak]]*l > ans) ans = heights[stack[peak]]*l;
        }
    }
    return ans;
}