def calcular_soma_produto(h1, h2, m1, m2):
    # Validando se as idades são inteiros positivos
    for idade in [h1, h2, m1, m2]:
        if not isinstance(idade, int) or idade <= 0:
            return "Erro: Todas as idades devem ser números inteiros positivos."
    
    # Determinando o homem mais velho e o homem mais novo
    if h1 > h2:
        homem_mais_velho = h1
        homem_mais_novo = h2
    else:
        homem_mais_velho = h2
        homem_mais_novo = h1

    # Determinando a mulher mais velha e a mulher mais nova
    if m1 > m2:
        mulher_mais_velha = m1
        mulher_mais_nova = m2
    else:
        mulher_mais_velha = m2
        mulher_mais_nova = m1

    # Calculando a soma e o produto conforme as regras
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha
    
    return {
        "soma": soma,
        "produto": produto
    }

# Exemplo de uso
h1 = 30  # Idade do primeiro homem
h2 = 25  # Idade do segundo homem
m1 = 28  # Idade da primeira mulher
m2 = 22  # Idade da segunda mulher

resultado = calcular_soma_produto(h1, h2, m1, m2)
if isinstance(resultado, dict):
    print(f"Soma do homem mais velho com a mulher mais nova: {resultado['soma']}")
    print(f"Produto do homem mais novo com a mulher mais velha: {resultado['produto']}")
else:
    print(resultado)
