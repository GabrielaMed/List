zodiaco = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre','Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
nasc = int(input("Insira o ano de seu nascimento para saber o seu signo do Zodíaco chinês: "))

result = nasc % 12

print(f"O seu signo do Zodíaco chinês é {zodiaco[result]}")