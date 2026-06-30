vetor=[2.5, 7,5, 10.0, 4.0]
#soma = sum(vetor) vai somar tudo que tem no vetor
soma = 0
for valor in vetor:
    soma += valor
media = soma / len(vetor) #vair achar a media 

proximo_da_media = vetor[0]
menor_distancia = abs(vetor[0] - media) #abs serve para dar valor absoluto
for valor in vetor:
    distancia_atual = abs(valor - media) 
    if distancia_atual < menor_distancia:
        menor_distancia = distancia_atual
        proximo_da_media = valor

print(f"Vetor: {vetor}")
print(f"Média: {media:.1f}")
print(f"Valor mais próximo da média: {proximo_da_media}")

print(media)