dados = {"SP" : 67836.43,"RJ": 36678.66,"MG" : 29229.88,"ES" : 27165.48,"Outros": 19849.53}
valores = [valores for valores in dados.values()]
total = sum(valores)
for chaves, valores in dados.items():
    print(f"Percentual de participação: {chaves} = {valores*100/total:.2f}%")