import json

# 1) Cálculo da variável SOMA
def calcular_soma(indice):
    soma = 0
    for k in range(1, indice + 1):
        soma += k
    return soma

# 2) Verificação de número na sequência de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a, b]
    while b < n:
        a, b = b, a + b
        fib_sequence.append(b)
    return fib_sequence

def pertence_fibonacci(num):
    fib_sequence = fibonacci(num)
    return num in fib_sequence

# 3) Cálculo de faturamento diário
def calcular_faturamento(faturamento_json):
    data = json.loads(faturamento_json)
    faturamento = data['faturamento']

    # Ignorar dias sem faturamento
    faturamento_validos = [valor for valor in faturamento if valor > 0]

    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    media_faturamento = sum(faturamento_validos) / len(faturamento_validos)

    dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media

# 4) Cálculo do percentual de faturamento por estado
def calcular_percentual_estado(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}
    return percentuais

# 5) Inversão de caracteres de uma string
def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# Exemplo de uso
if __name__ == "__main__":
    # 1) Cálculo da SOMA
    indice = 13
    print("SOMA de 1 a", indice, "é:", calcular_soma(indice))

    # 2) Verificação de Fibonacci
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

    # 3) Cálculo de faturamento diário
    faturamento_json = '''
    {
        "faturamento": [1500.00, 2000.00, 0.00, 3000.00, 2500.00, 0.00, 4000.00, 3500.00, 0.00, 4500.00]
    }
    '''
    menor, maior, dias_acima_media = calcular_faturamento(faturamento_json)
    print(f"Menor faturamento: R${menor:.2f}")
    print(f"Maior faturamento: R${maior:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")

    # 4) Cálculo do percentual de faturamento por estado
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    percentuais = calcular_percentual_estado(faturamento_estados)
    for estado, percentual in percentuais.items():
        print(f"Percentual de {estado}: {percentual:.2f}%")

    # 5) Inversão de string
    entrada = input("Informe uma string para inverter: ")
    print("String invertida:", inverter_string(entrada))