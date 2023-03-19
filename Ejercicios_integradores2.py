def minComMult(num1,num2):
    if (num1 <= 0) or (num2 <= 0):
        return 0
    

    if num1>num2:
       valorInicial=num1
       incremento=num1
       menorValor=num2
    else:
       valorInicial=num2
       incremento=num2
       menorValor=num1
    
    while ((valorInicial % menorValor) != 0 ):
        valorInicial += incremento

    
    return valorInicial

print(minComMult(3,44))
