texto = input("Informe um Texto:")
VOGAIS = "AEIOU"
contador = 0

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, "\n")

print()