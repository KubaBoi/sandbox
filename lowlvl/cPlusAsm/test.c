#include <stdio.h>

int myfunc(int param);

int main(void) {
    int ret;

    ret = myfunc(32);
    printf("myfunc(32) is %d\n", ret);

    return 0;
}
