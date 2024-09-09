# Sequência de Fibonacci

print("===== Pertence a sequência de Fibonacci? =====")
n = int(input("Digite um número para verificar: "))
t3 = 2
t4 = 3
aux = 0

# Caso base
if n <= 3:
    print(f"O número {n} pertence à sequência de Fibonacci")

else:
    # Calculando a sequência
    while t4 < n:
        aux = t4
        t4 = t3 + t4
        t3 = aux

    # Verificando se pertence à sequencia
    if n == t4 or n == t3:
        print(f"O número {n} pertence a sequência de Fibonacci")
    else:
        print(f"O número {n} não pertence a sequência de Fibonacci.")
