consoantes = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
vogais = ["A","E","I","O","U"]
cont = 0
for a in consoantes:
    for b in vogais:
        primeiraSilaba = a+b
        for c in consoantes:
            for d in vogais:
                segundaSilaba = c+d
                if c+d != primeiraSilaba:
                    for e in consoantes:
                        for f in vogais:
                            terceiraSilaba = e + f
                            if terceiraSilaba != primeiraSilaba and terceiraSilaba != segundaSilaba:
                                cont+=1

                                print(a+b+c+d+e+f, end = " ")
print(cont)
