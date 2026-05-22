# # 1

# def soma_elementos(a):
#     b = []
#     b.extend(a)
#     return sum(b)

# print(soma_elementos([1, 2, 3, 4]))

# # 2

# def e_palindromo(a):
#     if list(a) == list(reversed(a)):
#         return True
#     elif list(a) != list(reversed(a)):
#         return False
    
# print(e_palindromo("arara"))

# # 3

# def maior_elemento(a):
#     b = []
#     b.extend(a)
#     return max(b)

# print(maior_elemento([1, 2, 100, 4]))

# # 4

# def contar_caracteres(a, b):
#     return list(a).count(b)

# print(contar_caracteres("arraia", "r"))

# 5

def soma(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x*y
def div(x, y):
    return x/y

def menu():
    opcao = int(input(
        "Calculadora\n"
        "Escolha uma opção:\n"
        "1 - Soma\n"
        "2 - Subtração\n"
        "3 - Multiplicação\n"
        "4 - Divisão\n"
        "0 - Sair\n"
        "Digite aqui:\n"
    ))
    if opcao == 1:
        n = int(input("Insira seu número: "))
        m = int(input("Insira seu número: "))
        print("Resultado:", soma(n, m))
        menu()
    elif opcao == 2:
        n = int(input("Insira seu número: "))
        m = int(input("Insira seu número: "))
        print("Resultado:", sub(n, m))
        menu()
    elif opcao == 3:
        n = int(input("Insira seu número: "))
        m = int(input("Insira seu número: "))
        print("Resultado:", mult(n, m))
        menu()
    elif opcao == 4:
        n = int(input("Insira seu número: "))
        m = int(input("Insira seu número: "))
        print("Resultado:", div(n, m))
        menu()
    elif opcao == 0:
        print("Obrigado por testar, desenvolvido por Davi.")
    else:
        print("Opção selecionada inválida, escolha corretamente.")
        menu()

menu()
    




