#7- Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
#ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
#tabela:
#O programa deverá mostrar na tela o conceito correspondente e a mensagem
#“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
#Média de Aproveitamento Conceito
#Entre 9.0 e 10.0 A
#Entre 7.5 e 9.0 B
#Entre 6.0 e 7.5 C
#Entre 4.0 e 6.0 D
#Entre 4.0 e zero E

def determinar_conceito(media):
    if media >= 9.0:
        return 'A'
    elif media >= 7.5:
        return 'B'
    elif media >= 6.0:
        return 'C'
    elif media >= 4.0:
        return 'D'
    else:
        return 'E'

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

conceito = determinar_conceito(media)

if conceito in ['A', 'B', 'C']:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print(f"\nMédia: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")

print("\nTabela de Conceitos:")
print("A - Média ≥ 9.0")
print("B - 7.5 ≤ Média < 9.0")
print("C - 6.0 ≤ Média < 7.5")
print("D - 4.0 ≤ Média < 6.0")
print("E - Média < 4.0")