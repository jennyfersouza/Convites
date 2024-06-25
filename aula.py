def enviar_convites():
 print("Informe a quantidade de convites")

 convites = int(input())

 for i in range(convites):
    nome = input(f'Informe o nome do convidado de número {i+1}')
    print(f'Enviando convite para {nome}')
    
enviar_convites()
    