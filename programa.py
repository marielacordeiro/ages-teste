def par_ou_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é par."
    else:
        return f"{numero} é ímpar."

numero = int(input("Digite um número: "))

print(par_ou_impar(numero))
