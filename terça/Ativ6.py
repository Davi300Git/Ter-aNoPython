#6- Faça um programa em Python para uma loja de tintas. O programa deverá pedir o
#tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
#é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#compradas e o preço total.
#Obs: A quantidade de latas deverá ser um número inteiro. Utilize a biblioteca math:
#https://docs.python.org/3/library/math.html


COBERTURA_POR_LITRO = 3  
LITROS_POR_LATA = 18
PRECO_POR_LATA = 80.00

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area / COBERTURA_POR_LITRO
latas_necessarias = int(litros_necessarios / LITROS_POR_LATA)

if litros_necessarios % LITROS_POR_LATA > 0:
    latas_necessarias += 1

preco_total = latas_necessarias * PRECO_POR_LATA

print(f"\nPara pintar {area:.2f} m² você precisará de:")
print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")

litros_faltantes = litros_necessarios - ((latas_necessarias - 1) * LITROS_POR_LATA)
if latas_necessarias > 1:
    print(f"\nObservação: A última lata terá aproximadamente {litros_faltantes:.2f} litros utilizados dos 18 disponíveis.")
