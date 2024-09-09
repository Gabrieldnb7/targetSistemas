# Inverter uma string

texto = str(input("Digite uma frase: "))
textoInv = ""
for c in texto[::-1]:
    textoInv += c
print(textoInv)