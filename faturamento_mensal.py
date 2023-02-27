import json


meu_json = open("C:/Users/Felipe/Documents/Estudos autonomos/target/dados.json",'r')
dados = json.load(meu_json)

def menor_faturamento():
    #No enunciado não diz se é para ignorar os dias sem faturamento no calculo do menor valor, apenas no cálculo da média
    primeiro_elemento = dados[0]
    menor_valor = primeiro_elemento['valor']
    for elemento in dados[1:]:
        if elemento['valor'] < menor_valor:
            menor_valor = elemento['valor']
    return menor_valor

def maior_faturamento():
    maior_valor = 0
    for elemento in dados:
        if elemento['valor'] > maior_valor:
            maior_valor = elemento['valor']
    return maior_valor

def dias_acima_media(media):
    nmr_de_dias = 0
    for elemento in dados:
        if elemento['valor'] > media:
            nmr_de_dias+=1
    return nmr_de_dias



total_de_faturamento = 0
dias_faturados = 0
for elemento in dados:
    if elemento['valor'] > 0:
        total_de_faturamento = total_de_faturamento + elemento['valor']
        dias_faturados+=1
media = total_de_faturamento / dias_faturados

print(media)
print(menor_faturamento())
print(maior_faturamento())
print(dias_acima_media(media))
