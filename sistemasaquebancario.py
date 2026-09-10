while True:
    try:
        saldo = float(input("Digite o saldo da conta: "))
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        if valor_saque <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor_saque > saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")

    except ValueError as e:
        print(f"Erro: {e}")
    else:
        saldo_restante = saldo - valor_saque
        print(f"Saque realizado com sucesso! \nSaldo restante: {saldo_restante}")
        break
    finally:
        print("Operação bancária finalizada.")