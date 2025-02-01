// using recursion
function fibonacciRecursive(n) {
    if (n <= 0) return 0;
    if (n === 1) return 1;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Print first 10 Fibonacci numbers
for (let i = 0; i < 10; i++) {
    console.log(fibonacciRecursive(i));
}

// using iteration
function fibonacciIterative(n) {
    let a = 0, b = 1;
    for (let i = 0; i < n; i++) {
        console.log(a);
        [a, b] = [b, a + b];  // Swap values
    }
}

fibonacciIterative(10);  // First 10 Fibonacci numbers
