#5- Faça um programa em Python que solicite ao usuário sua altura e sexo, calcule e
#imprima o seu peso ideal. Utilize a seguinte convenção:
#▪ Para homens: (72.7*h) – 58
#▪ Para mulheres: (62.1*h) – 44.7

altura = float(input("Digite sua altura em metros (ex: 1.75): "))
sexo = input("Digite seu sexo (M para masculino ou F para feminino): ").upper()
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    sexo_extenso = "masculino"
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    sexo_extenso = "feminino"
else:
    print("Sexo inválido! Digite M para masculino ou F para feminino.")
    exit()
print(f"\nPara uma pessoa do sexo {sexo_extenso} com {altura}m de altura:")
print(f"O peso ideal é: {peso_ideal:.2f} kg")