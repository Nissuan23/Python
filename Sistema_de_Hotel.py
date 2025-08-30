cliente1=str(input('Insira seu nome:'))
idade1=int(input('Qual é a sua idade?'))
lista=['simples','dupla','luxo']
print('''{} temos 3 tipos de quartos: Simples, Duplo e Luxo.
Simples:R$100 por dia
Dupla:R$150 por dia
Luxo:R$200 por dia'''.format(cliente1))
quarto=str(input('Qual quarto você quer?')).lower()
dias=int(input('quantos dias você vai ficar na suite {}?'.format(quarto)))
simples=100*dias
dupla=150*dias
luxo=250*dias
if quarto=='simples':
 print('O valor ficará:R${}'.format(simples))
elif quarto=='dupla':
 print('O valor ficará:R${}'.format(dupla))
elif quarto=='luxo':
 print('O valor ficará:R${}'.format(luxo))
else:
  print('desculpas!')
