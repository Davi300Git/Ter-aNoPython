#2- Faça um programa em Python que recebe a idade de cada um dos 500 alunos de uma
#escola, matriculados no Ensino Médio. O algoritmo deverá verificar, calcular e imprimir:
#a) a quantidade de alunos que podem votar, ou seja, têm idade mínima de 16 anos.
#b) a média da idade dos alunos que não são eleitores
# Inicialização das variáveis

total_alunos = 5
alunos_podem_votar = 0
alunos_nao_eleitores = 0
soma_idade_nao_eleitores = 0
for i in range(1, total_alunos + 1):
    while True:
        try:
            idade = int(input(f"Digite a idade do aluno {i}: "))
            if idade > 0:  
                break
            else:
                print("Idade inválida. Digite um valor positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    if idade >= 16:
        alunos_podem_votar += 1
    else:
        alunos_nao_eleitores += 1
        soma_idade_nao_eleitores += idade

if alunos_nao_eleitores > 0:
    media_nao_eleitores = soma_idade_nao_eleitores / alunos_nao_eleitores
else:
    media_nao_eleitores = 0
print("\nResultados:")
print(f"a) Alunos que podem votar (16 anos ou mais): {alunos_podem_votar}")
print(f"b) Média de idade dos não eleitores: {media_nao_eleitores:.2f} anos")