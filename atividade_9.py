###
# atividade 9
# aluno: Apollo
# Data: 17/03/2024
###

nome_aluno = input("Digite o nome do aluno:")
media_para_aprovacao = 7
nota_prova1 = float(input("digite a nota da prova 1: ")) 
nota_prova2 = ((3 * media_para_aprovacao) - nota_prova1) / 2
print(f"A nota da prova 2 eh: {nota_prova2:.2f}")
nota_necessaria = ((media_para_aprovacao * 3) + nota_prova1) / 3
print(f"A nota necessária na segunda prova eh: {nota_necessaria:.2f}")

