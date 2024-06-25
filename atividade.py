print("Escolha uma opção: 1- Quantidade de caracteres, 2- Quantidade de palavras, 3- Sair.")
opcao = int(input())

while opcao < 5:
    if opcao == '1':
    print("Informe o texto: ")
    caracter = input()
    frase_sem_espacos = caracter.replace(" ","")
    print(f"O tamanho é: {len(frase_sem_espacos)}")
 
  elif opcao == '2':
    print("Informe a palavra: ")
    frase = input()
    quantidade_palavras = frase.split()
    print(f"Quantidade de palavras é: {len(quantidade_palavras)}")
 
  elif opcao == '3':
    print("Fechando sistema.")
    break