notas = []
alunos =[]

while True:
    aluno = input("Nome ou 0 para sair: ")
    if aluno == "0":
        break
    alunos.append(aluno)
    
    for idx in range(1,4):
        nota = float(input(f"Digite a sua {idx} nota: "))
        notas.append(nota)
    print(f"\n------------- Média -------------\nA média do(a) aluno(a) {aluno} foi {(sum(notas))/3:.2f}")