while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
        break
    except ValueError:
        print("Erro: Por favor, digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
        print("Operação finalizada.")