#include <stdio.h>

void minus(int v, int n) {
    int k = v - n;
    printf("%d", k);
}

int main() {
    int v, n;
    scanf("%d %d", &v, &n);
    minus(v, n);
    return 0;
}