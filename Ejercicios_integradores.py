def maxComunDivisor(num1,num2):
    menorValor=num1 
    if num2<menorValor:
       menorValor=num2
    
    for i in range(menorValor,1,-1):
        if (num1 % i) == 0 and (num2 % i) == 0:
            return i

    return 0

print(maxComunDivisor(-1,300))

print(maxComunDivisor(225,300))
print(maxComunDivisor(300,225))

