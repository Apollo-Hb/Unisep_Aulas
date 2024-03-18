###
# atividade 6
# aluno: Apollo
# Data: 17/03/2024
###

QH = float(input("Digite a quantidade de hamburguer:" ))
QC = float(input("Digite a quantidade de chessehamburguer:" ))
QF = float(input("Digite a quantidade de fritas:" ))
QR = float(input("Digite a quantidade de refrigerante:" ))
QM = float(input("Digite a quantidade de milkshake:" ))
T = (QH * 3.00) + (QC * 2.50) + (QF * 2.50) + (QR * 1.00) + (QM * 3.00)
print(f"o valor total da conta: {T:.2f}")

