
def soma():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Soma:", x + y)

def subtracao():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Subtração:", x - y)

def multiplicacao():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Multiplicação:", x * y)

def divisao():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Divisão:", x / y)

opcao = 1
while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão")
    opcao = int(input("Opção: "))
    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
