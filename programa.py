def soma_numeros(n):
    return sum(range(1, n + 1))

try:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 1:
        print("Por favor, digite um número positivo.")
    else:
        resultado = soma_numeros(numero)
        print(f"A soma dos números de 1 até {numero} é: {resultado}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")