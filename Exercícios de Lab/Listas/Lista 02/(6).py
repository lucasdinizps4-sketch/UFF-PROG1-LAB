# Dada a lista valores = [25, 14, 89, 7, 42, 95, 63, 95, 22], escreva um programa que encontre o segundo maior valor presente na lista.
# Restrição: Você não pode usar funções de ordenação como sort() ou sorted() para resolver este problema. A lógica deve ser implementada usando um laço de
# repetição.
# Dica: Você precisará de duas variáveis para guardar o maior e o segundo maior valor enquanto percorre a lista.




valores = [25, 14, 89, 7, 42, 95, 22] 
maior = float("-inf")
s_maior = float("-inf") 

for i in valores: 
 if i > maior: 
  s_maior = maior 
  maior = i 
  
 elif i > s_maior and i != maior: 
  s_maior = i 

print(s_maior) 






            
    
 
 

