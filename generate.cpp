#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int f=0;
    int x=1000;
    srand(time(NULL));
    while(f<150){
        f++;
        if(f==150)
            break;
        string fn="file_"+to_string(f);
        fn=fn+".txt";
        freopen(fn.c_str(),"a",stdout);
        clock_t begin = clock();
        //int t=rand()%1000 + 1;
        int t=1;
        //cout<<t<<endl;
        if(f%50==0)
            x=x*10;
        while(t--){
            int k=rand()%x+1;
            int n=rand()%x + 1;
            n = min((k*(k-1))/2, n);
            printf("%d\n", n);
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
    }
    fclose(stdout);
    freopen("/dev/tty","w+",stdout);
    return 0;
}