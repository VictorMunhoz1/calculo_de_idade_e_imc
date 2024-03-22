nome = input('Olá, por favor, digite seu nome: ')
ano_atual = int(input('Digite o ano atual:  '))
ano_nascimento = int(input(f'Por favor {nome}, digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

print(f'Prazer em te conhecer {nome}!')
print(f'Com base nas informações fornecidas, o ano atual é {ano_atual}.')
print(f'O seu ano de nascimento é {ano_nascimento} e sua idade são {idade} anos.')

altura = float(input(f'{nome}, quantos metros você tem: '))
peso = float(input('Sei que essa é uma pergunta indelicada, mas poderia me informar o seu peso: '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'{nome},seu IMC é {imc:.2f}, procure um médico, você está abaixo do seu peso ideal.')
elif imc >= 18.6 and imc <= 24.9:
    print(f'{nome}, seu IMC é {imc:.2f}, você está no seu peso ideal, parabéns!!!')
elif imc >= 25 and imc <= 29.9:
    print(f'{nome}, seu IMC é {imc:.2f}, você está com excesso peso!!!')
elif imc >= 30 and imc <= 34.9:
    print(f'{nome}, seu IMC é {imc:.2f}, você está obeso. Cuidado!!!')
else:
    print(f'{nome}, seu IMC é {imc:.2f}, você está com obesidade morbida. FAVOR PROCURAR UM MÉDICO COM URGENCIA!')
    



      
      
       
