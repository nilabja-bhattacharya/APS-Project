#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    clock_t begin = clock();
    freopen("infile.txt","w",stdout);
    srand(time(NULL));
    //int t=rand()%1000 + 1;
    int t=1;
    //cout<<t<<endl;
    while(t--){
        int n=rand()%1000 + 1;
        printf("%d\n", n);
        int k=rand()%1000+1;
        printf("%d\n",k);
        for(long long int i=0;i<n;i++){
            int lowerLimit = 1, upperLimit = 1e9+7;
            int u = rand() % k + 1;
            int v = rand() % k + 1;
            int w =  lowerLimit + rand() % (upperLimit - lowerLimit);
            printf("%d\n%d\n%d\n", u,v,w);
        }
        clock_t end = clock();
        double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
        //printf("\n");
        //printf("%f\n",time_spent);
    }
    fclose(stdout);
    freopen("/dev/tty","w+",stdout);
    return 0;
}