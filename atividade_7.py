###
# atividade 7
# aluno: Apollo
# Data: 17/03/2024
###
                                                    
nome_vendedor = input("Informe o nome do vendedor: ")
num_carros_vendidos = float(input("Informe o número de carros vendidos: "))
valor_total_vendas = float(input("Informe o valor total das vendas: "))

salario = 500.0
comissao_por_carro = 50.0
comissao_por_venda = 0.05 * valor_total_vendas

salario_total = salario + (comissao_por_carro * num_carros_vendidos) + comissao_por_venda

print(f"salario total: {salario_total:.2f}")