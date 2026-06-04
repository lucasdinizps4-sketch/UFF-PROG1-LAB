arq = open("turma.txt","r") 
dados = arq.readlines()
arq.close()
 
saida = open("media.txt","w")
saida.write("Nome","Média") 
for i in range(1,len(dados)): 
  aluno = dados[i].split(",")
  nome = aluno[0] 
  soma = 0 
  for j in range(1,len(aluno)): 
   soma += float(aluno[j])
  media = soma / (len(aluno) - 1)
  linha = nome + "," + str(media) + "\n"
  saida.write(linha)