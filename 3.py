# Leitura de dados em json

import json

def menorFaturamento(vetor):
    with open(f"{vetor}", "r") as dados:
        faturamentoMensal = json.load(dados)
    # List comprehension com os valores do dia
    valorFaturamento = [dia['valor'] for dia in faturamentoMensal]
    return min(valorFaturamento)

def maiorFaturamento(vetor):
    with open(f"{vetor}", "r") as dados:
        faturamentoMensal = json.load(dados)
    valorFaturamento = [dia['valor'] for dia in faturamentoMensal]
    return max(valorFaturamento)

def mediaSuperior(vetor):
    with open(f"{vetor}", "r") as dados:
        faturamentoMensal = json.load(dados)
    valorFaturamento = [dia['valor'] for dia in faturamentoMensal]
    contador = 0
    # List comprehension com o faturamento acima de 0
    vetorFaturamento = [valor for valor in valorFaturamento if valor > 0]
    media = sum(vetorFaturamento) / len(vetorFaturamento)
    print(media)
    for dia in valorFaturamento:
        if dia > media:
            contador += 1
    return (f"{contador} dias obtiveram uma média de faturamento diário maior que a mensal")

tabela = "dados.json"
print(menorFaturamento(tabela))
print(maiorFaturamento(tabela))
print(mediaSuperior(tabela))