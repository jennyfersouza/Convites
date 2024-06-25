def enviar_convites():
 print("informe quantidade de convites:")

 convites = int(input())
 contador = 0

 while contador < convites:
    nome = input(f'Informe o nome do convidado: {contador +1}')
    print (f'Enviando convite para {nome}')
    contador +1
    
enviar_convites()