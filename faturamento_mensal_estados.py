def calcula_porcentagem(estado, total):
    porcentagem_estado = (estado * 100) / total
    return porcentagem_estado


sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros

print("SP - %.2f%%" % calcula_porcentagem(sp, total))
print("RJ - %.2f%%" % calcula_porcentagem(rj, total))
print("MG - %.2f%%" % calcula_porcentagem(mg, total))
print("ES - %.2f%%" % calcula_porcentagem(es, total))
print("Outros - %.2f%%" % calcula_porcentagem(outros, total))
