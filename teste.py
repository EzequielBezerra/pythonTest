import math

# Exibindo uma mensagem de boas-vindas
print('Olá, seja bem vindo')

# Solicitando ao usuário que escolha a operação
print('Escolha a operação matemática:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Raiz Quadrada')

entrada = input('Digite o número da operação desejada: ')

# Verificando qual operação o usuário escolheu
if entrada == '1':  # Adição
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 + num2
    print(f'O resultado de {num1} + {num2} é {resultado}')

elif entrada == '2':  # Subtração
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 - num2
    print(f'O resultado de {num1} - {num2} é {resultado}')

elif entrada == '3':  # Multiplicação
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 * num2
    print(f'O resultado de {num1} * {num2} é {resultado}')

elif entrada == '4':  # Divisão
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    # Vamos garantir que o divisor não seja zero
    if num2 != 0:
        resultado = num1 / num2
        print(f'O resultado de {num1} / {num2} é {resultado}')
    else:
        print('Erro: Divisão por zero não é permitida!')

elif entrada == '5':  # Raiz Quadrada
    num = float(input('Digite um número: '))
    if num >= 0:
        raiz = math.sqrt(num)
        print(f'A raiz quadrada de {num} é {raiz}')
    else:
        print('Erro: Não é possível calcular a raiz quadrada de um número negativo!')

else:
    print('Operação inválida. Por favor, escolha um número de 1 a 5.')