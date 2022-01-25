votes = [0]*23
totalvotes = winner = porcentagem = 0

print("Enquete: Quem foi o melhor jogador?")

while True:
    vote = int(input("Digite o número correspondente a camisa do jogador: "))
    if vote < 0 or vote > 23: print("ERROR. O número digitado é inválido.")
    if vote == 0: break 
    votes[vote - 1] += 1
 
for  vote in votes: totalvotes +=  vote

print(f"\nResultado da votação:\nForam computados {vote} votes.")
print("Jogador      Votos            %")

for idx, vote in enumerate(votes):
    if vote > 0:
        porcentagem = (vote*100)/totalvotes
        print(f"   {idx+1}           {vote}            {round(porcentagem,1)}%")
        if vote > votes[winner]: winner = idx

print(f"O melhor jogador foi o número {winner+1},  com {votes[winner]} votos, correspondendo a {round((votes[winner]*100)/totalvotes, 1)}% do total dos votos.")