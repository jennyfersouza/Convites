print("Escolha uma opção: 1- Quantidade de caracteres, 2- Quantidade de palavras, 3- Sair.")
opcao = int(input())

while opcao < 5:
    if opcao == 1:
        print("Informe o texto:")
        texto = input()
        print("O tamanho é: " + len(texto))
    elif opcao == 2:
        print("Informe o texto: ")
        frase = input()
        palavra = frase.split()
        print("Quantidade de palavras é: " + len(palavra))   
    elif opcao == 3:
        print("Você está deixando o sistema.")
        break