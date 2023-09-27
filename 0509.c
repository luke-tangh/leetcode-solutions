int fib(int n){
    if (n == 0){
        return 0;
    }
    long a = 1, b = 1;
    n -= 1;
    while (n--){
        a = (b += a) - a;   
    }
    return a;
}