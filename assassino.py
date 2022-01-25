answer = []
print("--- Responda as seguintes perguntas apenas com sim ou não ---")

um = input("Você telefonou para a vítima? ")
dois = input("Você esteve no local do crime? ")
tres = input("Você mora perto da vítima? ")
quatro = input("Você tinha dívidas com a vítima? ")
cinco = input("Você já trabalhou com a vítima? ")
answer.append(um)
answer.append(dois)
answer.append(tres)
answer.append(quatro)
answer.append(cinco)

cont = answer.count('sim')
if cont == 5: print("Sua classificação é: Assassino.")
elif cont == 3 or cont == 4: print("Sua classificação é: Cúmplice.")
elif cont == 2: print("Sua classificação é: Suspeita.")
else: print("Sua classificação é: Inocente.")