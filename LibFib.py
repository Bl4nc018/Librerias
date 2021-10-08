def fib(n): #serie de fibonacci mediante una función.    
    a, b = 0, 1 # a = 0 |  b = 1
    while a < n: #while se usa para bucles infinitos o hasta que lleguen a cierto valor.
        print(a, end=' ')
        a, b = b, a+b #temporal = a | a = b |  b = temporal + b
    print()
fib (2000)