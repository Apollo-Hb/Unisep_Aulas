###
# atividade 8
# aluno: Apollo
# Data: 17/03/2024
###

nome_aluno = input("Digite o nome do aluno:")
nota_qualitativa = float(input("digite a nota da prova qualitativa: "))
nota_prova = float(input("Digite a nota da prova: "))
Media = (nota_qualitativa + (nota_prova * 2)) / 3

print(f"A media final do aluno eh: {Media:.2f}")
