def calc_combustivel(distancia, combustivel_gasto):
    consumo_medio = distancia / combustivel_gasto
    result = {
        "Distancia Percorrida": f"{distancia} KM",
        "Combustivel Gasto": f"{combustivel_gasto} litros",
        "Consumo médio": f"{consumo_medio:.2f} km/l"
    }

    return result


if __name__ == "__main__":
    print(calc_combustivel(300, 25))