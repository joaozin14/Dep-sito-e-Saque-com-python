print()

from time import sleep

saldo_conta = 0  # Define o saldo inicial
contador_deposito = 0 # Contador do depósito
contador_saque = 0 # Contador do saque

# Função que faz o depósito
def depositar():
    global saldo_conta
    global contador_deposito
    saldo = float(input("Digite o valor do depósito: R$"))
    print()
    novo_saldo = saldo_conta + saldo  # Soma o depósito ao saldo atual
    print("Depositando valor...")
    print()
    sleep(2)
    saldo_conta = novo_saldo  # Atualiza o saldo global
    print(f"Depositado R${saldo}. Seu novo saldo é R${novo_saldo}")
    print() 
    contador_deposito += 1
    print(f"Seus depósitos {contador_deposito}")
    print()

# Função que faz o saque 
def sacar():
    global saldo_conta
    global contador_saque
    saque = float(input("Quanto deseja sacar?: R$"))
    print()
    
    if saque > saldo_conta:  # Verifica se o saque é maior que o saldo
        print("Saldo insuficiente!")
        print()
        return

    novo_saldo = saldo_conta - saque  # Subtrai o valor sacado do saldo atual
    print("Fazendo o saque...")
    print()
    sleep(2)
    saldo_conta = novo_saldo  # Atualiza o saldo global
    print(f"Foi sacado R${saque}. Seu novo saldo é R${novo_saldo}")
    print()
    contador_saque += 1
    print(f"Seus saques {contador_saque}")
    print()


# Loop principal
while True:
    opcao = input("Se deseja fazer um depósito, digite 1 ou se deseja sacar (caso não tenha excedido o número de saques), digite 2, ou se deseja cancelar, digite 3: ")
    print()
    if opcao == "1":
        depositar()
    elif opcao == "2":
        if contador_saque == 3:
            print("Número excedido de saques")
            print
            continue
        sacar()
    elif opcao == "3":
        if contador_deposito <= 1:
            print(f"Seu depósito foi de {contador_deposito} e {contador_saque} saques")
        else:    
            print(f"Seus depósitos foram {contador_deposito} e {contador_saque} saques")
        print()
        print("Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")