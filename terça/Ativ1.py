#1- Escreva um programa em Python que resolva o
#problema: “Um Programador com insônia”,
#representado ao lado. Utilize o comando de
#repetição apropriado para o problema.
#Obs: Exibir no final o número de carneirinhos
#contados.
# Programa: Contando carneirinhos até o usuário dizer que dormiu
totalCarnei = 0
dormindo = False 
while not dormindo:
    totalCarnei += 1
    print("Contando carneirinho",totalCarnei)
    resposta = input("O programador já dormiu? (s/n): ").strip().lower()
    if resposta == 's':
        dormindo = True
print("\nO programador adormeceu após contar",totalCarnei," carneirinhos!")