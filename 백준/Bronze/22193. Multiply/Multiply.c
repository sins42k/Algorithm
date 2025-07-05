#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_DIGITS 50002 // Maximum possible digits + buffer

int main() {
    int n, m;
    char s1[MAX_DIGITS], s2[MAX_DIGITS];
    int num1[MAX_DIGITS] = {0}, num2[MAX_DIGITS] = {0}, result[MAX_DIGITS * 2] = {0};
    int len1, len2, len_res;
    int i, j;

    // Read N and M (lengths of the numbers), but we can also use strlen
    scanf("%d %d", &n, &m);
    scanf("%s", s1);
    scanf("%s", s2);

    len1 = strlen(s1);
    len2 = strlen(s2);

    // Convert char strings to int arrays in reverse order
    for (i = 0; i < len1; i++) {
        num1[i] = s1[len1 - 1 - i] - '0';
    }
    for (i = 0; i < len2; i++) {
        num2[i] = s2[len2 - 1 - i] - '0';
    }

    // Multiplication
    for (i = 0; i < len2; i++) {
        for (j = 0; j < len1; j++) {
            result[i + j] += num2[i] * num1[j];
        }
    }

    len_res = len1 + len2;

    // Handle carries
    for (i = 0; i < len_res; i++) {
        if (result[i] >= 10) {
            result[i + 1] += result[i] / 10;
            result[i] %= 10;
        }
    }

    // Find the start of the result
    while (len_res > 1 && result[len_res - 1] == 0) {
        len_res--;
    }

    // Print the result in reverse order
    for (i = len_res - 1; i >= 0; i--) {
        printf("%d", result[i]);
    }
    printf("");

    return 0;
}