def oklidMesafe(a1,a2):
    oklid = 0

    for x in range(len(a1)):
        oklid += (a1[x]- a2[x])*(a1[x]- a2[x])
    oklid **= (1/2)
    return oklid

matris1 = [-1, 2, 1]
matris2 = [-1, 4, 6]
sonuc = oklidMesafe(matris1,matris2)
print(sonuc)