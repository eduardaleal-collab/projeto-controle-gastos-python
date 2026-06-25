print("=== CONTROLE DE GASTOS ===")

gastos = []

for i in range(5):

    valor = float(
        input(f"Digite o gasto {i+1}: ")
    )

    gastos.append(valor)

total = sum(gastos)

media = total / len(gastos)

maior = max(gastos)

menor = min(gastos)

print("\nRESULTADO")

print("Gastos:", gastos)

print("Total:", total)

print("Média:", media)

print("Maior gasto:", maior)

print("Menor gasto:", menor)
