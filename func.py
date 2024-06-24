def get_numbers(romano):
    resp = input("Coloque um algarismo romano -> ")
    romano.extend(resp)
    if romano.count("I") > 3 or romano.count("V") > 3 or romano.count("X") > 3 or romano.count("L") > 3 or romano.count("C") > 3 or romano.count("D") > 3 or romano.count("M") > 3:
        print("Número não existe")
        exit()

def converter(romano, resposta):
    for counter in range(len(romano)):
        alg = romano.pop()
        if alg == "I": resposta.append(1)
        elif alg == "V": resposta.append(5)
        elif alg == "X": resposta.append(10)
        elif alg == "L": resposta.append(50)
        elif alg == "C": resposta.append(100)
        elif alg == "D": resposta.append(500)
        elif alg == "M": resposta.append(1000)            
            
def conta(resposta):
    res2 = 0
    if resposta[0] > resposta[1]:    
        resposta.reverse()
        for counter in range(len(resposta)):
            res2 = resposta[1] - resposta[0]
        return res2 
    else:
        for counter in range(len(resposta)):
            parcial = resposta.pop()
            res2 += parcial
        return res2