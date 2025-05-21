def calc_media_escolar(notas:list):
    soma_notas = 0
    for i in notas:
        soma_notas += i
    
    media = soma_notas / len(notas)

    result = {
        "notas": notas,
        "média": f"{media:.2f}"
    }

    return result

if __name__ == "__main__":
    notas1 = [7.5, 8, 6.5]
    print(calc_media_escolar(notas1))