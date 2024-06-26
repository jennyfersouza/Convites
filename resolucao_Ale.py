while True:
    print("Programa para contagem de caracteres ou número de palavra")
    print("1 - contar número caracter")
    print("2 - contar número de palavras")
    print("3 - sair do sistema")
 
    escolha = input("Digite a opção desejada")
 
    if escolha == "3":
        print("Saindo do sistema...")
        break
    elif escolha in {"1", "2"}:
        texto = input("Digite o texto: ")
 
        if escolha == "1":
            texto_sem_espacos = texto.replace(" ", "")
            qtd = len(texto_sem_espacos)
            opcao = "Caracteres"
        elif escolha == "2":
            palavras = texto.split()
            qtd = len(palavras)
            opcao = "Palavras"
 
        print(f"existem {qtd} {opcao} no seu texto")
    else:
        print("Escolha uma opção valida")