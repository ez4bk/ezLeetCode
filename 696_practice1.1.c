#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
#include <stdint.h>

int noNameFunc2(int c, int s){

    if (c == 1){
        return s;
    } else{
        return noNameFunc2(c - 1, s * c);
    }

}

int noNameFunc1(int n){
    if (n == 0){

        return 1;
    }
    return noNameFunc2(n, 1);
}

int main(){
    printf("%d", noNameFunc1(10));
    return 1;
}
