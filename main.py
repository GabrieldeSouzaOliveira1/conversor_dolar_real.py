from convertor import dolareal, realdolar #Importa as funções do .py chamado "convertor"


#Introdução ao sistema:
print("-="*20)
print("Sistema de conversão de moedas")
print("-="*20)

# Loop para se usuario queira continuar no comando
while True:
  # Exibe as opções disponíveis para o usuário
  print("""
  Para converter Dolar para real digite [ 1 ]
  Para converter Real para Dolar digite [ 2 ]
  Para sair do comando digite [ 0 ]
  """)
  try:
    
    # Solicita a escolha do usuário
    resp = int(input("\nDigite Qual das duas opções você quer escolher: "))
    print("-="*30)
    
    # Verifica a escolha do usuário e chama a função correspondente
    if resp == 1:
      # Chama a função "realdolar" para converter Real para Dólar
      realdolar(valordolar=None,n1=None)
    elif resp == 2:
      # Chama a função "dolareal" para converter Dólar para Real
      dolareal(valordolar=None,valoreal=None)
    else:
      # Mensagem de erro caso o usuário digite um valor inválido
      print("\nValor  invalido")

    # Pergunta ao usuário se deseja continuar ou sair
    sair = input("\nDeseja fazer outra conversão? (S/N): ").strip().lower()
    if sair in 'n':
        print("\nSaindo do sistema... Até mais!")
        break  # Sai do loop e encerra o programa
  except ValueError:
    # Tratamento de erro caso o usuário digite algo que não seja um número inteiro
    print("\nDigite um numero inteiro!!!")

