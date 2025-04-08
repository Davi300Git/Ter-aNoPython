#4- Faça um programa em Python que solicite ao usuário uma quantidade de segundos,
#calcule e exiba a quantidade de horas, minutos e segundos.

segundos_totais = int(input("Digite a quantidade de segundos: "))
horas = segundos_totais // 3600
segundos_restantes = segundos_totais % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60
print(f"\n{segundos_totais} segundos equivalem a:")
print(f"{horas} horas, {minutos} minutos e {segundos} segundos")