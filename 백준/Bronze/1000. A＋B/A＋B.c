#include<stdio.h>

void Add(int v, int n) {
    int k = v + n;
    printf("%d", k);
}

int main() {
    int v, n;
    scanf("%d %d", &v, &n);
    Add(v, n);
    return 0;
}