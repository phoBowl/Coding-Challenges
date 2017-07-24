int dim(long n) {
    int counter = 0;
    if(n == 0) return 1;
    while(n>0){
        n= n/2;
        counter++;
    }
    return counter;
}
