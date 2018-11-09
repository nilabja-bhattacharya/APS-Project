#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main()
{
    clock_t begin = clock();
    freopen("outfile.txt","w",stdout);
    for(long long int i=0;i<1000;i++){
        int lowerLimit = 1, upperLimit = 1e9;
        int r =  lowerLimit + rand() % (upperLimit - lowerLimit);
        printf("%d\n", r);
    }
    fclose(stdout);
    freopen("/dev/tty","w+",stdout);
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f\n",time_spent);
    return 0;
}