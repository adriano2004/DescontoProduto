p=float(input('Qual o preço do produto? '))
d=5.0 # 5% de desconto
valor= p-((p*d)/100) # calcula o desconto

print('O produto custa R$ {} com 5% de desconto'.format(valor))