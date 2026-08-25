class Recursion:
    def factorial(n):
        if n == 0 or n == 1:
            print(n)
            return 1

        print(n)
        return n * Recursion.factorial(n - 1)
    
    def fibonacci(n):
        if n==0:
            return 0
        if n==1:
            return 1
        
        return Recursion.fibonacci(n-1) + Recursion.fibonacci(n-2)
     
   
print("Fibonacci", Recursion.fibonacci(6))     
print("Factorial", Recursion.factorial(5))
