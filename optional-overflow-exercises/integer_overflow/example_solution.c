#include<stdio.h>
#include<limits.h>

void foo(int a, int b)
{
    printf("a = %d, b = %d, ", a, b);
    if (a > 0 && b > 0) {
        if (b > INT_MAX / a) {
            puts("Overflow error");
            return;
        }
    } else if (a > 0 && b < 0) {
        if (b < INT_MIN / a) {
            puts("Overflow error");
            return;
        }
    } else if (a < 0 && b > 0) {
        if (a < INT_MIN / b) {
            puts("Overflow error");
            return;
        }
    } else if (a < 0 && b < 0) {
        if (b < INT_MAX / a) {
            puts("Overflow error");
            return;
        }
    }
    printf("a * b = %d\n", a * b);
}

int main(void)
{
    int a, b;
    for(a = 10, b = 5; a < INT_MAX / 10; a *= 10, b *= 10)
    {
        foo(a,b);
    }
    for(a = 10, b = -5; a < INT_MAX / 10; a *= 10, b *= 10)
    {
        foo(a,b);
    }
    for(a = -10, b = 5; a > INT_MIN / 10; a *= 10, b *= 10)
    {
        foo(a,b);
    }
    for(a = -10, b = -5; a > INT_MIN / 10; a *= 10, b *= 10)
    {
        foo(a,b);
    }
    printf("INT_MAX = %d\n", INT_MAX);
    return 0;
}
