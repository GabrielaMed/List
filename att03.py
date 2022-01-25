print("Projeção de Gastos com Abono\n=============================\n")
salarios = [] 
abonos = minimo = maior = totalColab = 0

while True:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    salarios.append(salario)
    totalColab += 1

print("\nSalário - Abono\n")

for idx, salario in enumerate(salarios):
    abono = (salario * 20)/100

    if abono <= 100:
        abono = 100
        minimo += 1

    if abono > 100:
        abono = abono

    if abono > maior:
        maior = abono
    abonos += abono

    print(f"R${salarios[idx]} - R${abono}")

print(f"Foram processados {totalColab} colaboradores")
print(f'Total gasto com abonos: R${abonos}')
print(f"Valor mínimo pago a {minimo} colaboradores")
print(f"Maior valor de abono pago: R${maior}")