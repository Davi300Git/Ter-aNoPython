#3- Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um
#programa em Python que receba o salário fixo do funcionário e o valor de suas vendas,
#calcule e mostre a comissão e o salário final do funcionário.

salario_fixo = float(input("Digite o salário fixo do funcionário: R$ "))
valor_vendas = float(input("Digite o valor total das vendas: R$ "))
comissao = valor_vendas * 0.04  
salario_final = salario_fixo + comissao
print("\n--- Folha de Pagamento ---")
print(f"Salário fixo: R$ {salario_fixo:.2f}")
print(f"Comissão (4% sobre vendas): R$ {comissao:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")