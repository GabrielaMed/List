print("Qual o melhor Sistema Operacional para uso em servidores?\n\nAs possíveis respostas são:\n1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro")
votes = [0]*6
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
totalVotes = winner = 0

while True:
    vote = int(input("Digite o melhor Sistema Operacional em sua opinião: "))
    if vote < 0 or vote > 6: print("O número digitado é inválido.")
    if vote == 0: break
    votes[vote - 1] += 1

for vote in votes: totalVotes +=  vote

print("\nVotação encerrada!\n\nSistema Operacional      Votos            %")

for idx, vote in enumerate(votes):
    if vote > 0:
        porcentagem = (vote*100)/totalVotes
        print(f"{sistemas[idx]:<15}              {(vote):<6}            {(round(porcentagem,1)):>}%")
        if vote > votes[winner]: winner = idx

print(f"\nTotal                      {totalVotes:<22}\nO Sistema Operacional mais votado foi o {winner+1},  com {votes[winner]} votos, correspondendo a {round((votes[winner]*100)/totalVotes, 1)}% dos votos.")