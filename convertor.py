from cotação_atual import cotacao # importa a cotação do Dolar para Real Atualizada


#Função para converter Real para Dolar:
def dolareal(valordolar,valoreal):
  valordolar = cotacao #Valor do Dolar para real Atualizado
  valoreal= int(input("\nuantos reais você quer converter para Dolar: "))
  conta = valoreal / valordolar  #Calculo para converter Real em Dolar , [ Real dividido por Dolar]
  print(f"\nCom {valoreal} reais você compra {(conta)} dólares")

#Função para converter Dolar para Real:
def realdolar(valordolar,n1):
  valordolar = cotacao  #Valor do Dolar para real Atualizado
  n1 = int(input("\nQuantos Dólares vocẽ quer converter para Real: "))
  conta = valordolar * n1  #Calculo para converter Real em Dolar , [ Dolar Multiplicado por Real]
  print(f"\nCom {n1} Dólares você compra {(conta )} Reais. ")
