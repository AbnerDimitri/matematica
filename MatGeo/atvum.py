def calcular_salario(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos):
    # Define a porcentagem sobre o total das vendas e o bônus
    percentual_sobre_vendas = 0.05
    bonus_percentual = 0.10 if carros_vendidos > 10 else 0.0
    
    # Calcula o salário baseado nas condições da tabela verdade
    if carros_vendidos == 0:
        # Caso 1: Nenhuma venda, apenas salário fixo
        salario_final = salario_fixo
    elif carros_vendidos > 0 and carros_vendidos <= 10:
        # Caso 2: Vendeu entre 1 e 10 carros, recebe salário fixo, comissão e percentual sobre vendas
        salario_final = (
            salario_fixo + 
            (comissao_por_carro * carros_vendidos) + 
            (percentual_sobre_vendas * total_vendas)
        )
    else:
        # Caso 3: Vendeu mais de 10 carros, recebe salário fixo, comissão, percentual e bônus
        salario_final = (
            salario_fixo + 
            (comissao_por_carro * carros_vendidos) + 
            (percentual_sobre_vendas * total_vendas) + 
            (bonus_percentual * total_vendas)
        )
    
    return salario_final

# Exemplo de uso
salario_fixo = 2000  # Salário fixo mensal
comissao_por_carro = 250  # Comissão fixa por carro
total_vendas = 50000  # Valor total das vendas
carros_vendidos = 12  # Número de carros vendidos

salario_final = calcular_salario(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos)
print(f"Salário final do vendedor: R$ {salario_final:.2f}")
