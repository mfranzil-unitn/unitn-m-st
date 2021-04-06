#include<stdio.h>
#include<limits.h>

void foo(int a, int b)
{
    printf("a = %d, b = %d, ", a, b);
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
