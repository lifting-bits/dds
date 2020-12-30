#include <stdio.h>
#include <stdlib.h>

int __attribute__((noinline)) function1(int a, int b)
{
	if (a <= b)
		return a;
	a -= b;
	return function1(a, b);
}

int __attribute__((noinline)) function2(int a, int b, int c)
{
	a *= c;
	return function1(a, b);
}

int main(int argc, char *argv[])
{
	int res;

	if (argc < 3)
		return -1;

	res = function2(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]));
	printf("Result is %d\n", res);

	return 0;
}