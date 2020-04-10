#variável
salario = float(input('Digite o valor do seu salário: R$ '))
aumento20 = 20 / 100
aumento15 = 15 / 100
aumento10 = 10 / 100
aumento5 = 5 / 100
#cálculo e mostrar na tela
if(salario < 280.00):
  v_aumento = salario * aumento20
  total = salario + v_aumento
  print('Seu antigo salário era:R$ ', salario)
  print('O percentual do seu reajuste é: 20%')
  print('O valor do aumento é:R$ ',v_aumento)
  print('O seu novo salário é:R$ ',total)
elif(salario >= 280.00 and salario <= 700.00):
  v_aumento = salario * aumento15
  total = salario + v_aumento
  print('Seu antigo salário era:R$ ', salario)
  print('Seu antigo salário era:R$ ', salario)
  print('O percentual do seu reajuste é: 15%')
  print('O valor do aumento é:R$ ',v_aumento)
  print('O seu novo salário é:R$ ',total)
elif(salario >= 700.00 and salario <= 1500.00):
  v_aumento = salario * aumento10
  total = salario + v_aumento
  print('Seu antigo salário era:R$ ', salario)
  print('O percentual do seu reajuste é: 10%')
  print('O valor do aumento é:R$ ',v_aumento)
  print('O seu novo salário é:R$ ',total)
else:
  v_aumento = salario * aumento5
  total = salario + v_aumento
  print('Seu antigo salário era:R$ ', salario)
  print('O percentual do seu reajuste é: 5%') 
  print('O valor do aumento é:R$ ',v_aumento)
  print('O seu novo salário é:R$ ',total) 
