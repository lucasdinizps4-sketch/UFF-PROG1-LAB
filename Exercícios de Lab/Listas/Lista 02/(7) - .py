n = int(input())
if n <1:
    print("Número inválido")
elif n == 1:
    print("[0]")
else:
    fib = [0,1]
    for i in range(n):
        fib.append(fib[i] + fib[i+1])
print(fib)
