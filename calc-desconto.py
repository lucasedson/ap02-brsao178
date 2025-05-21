def calcula_desconto(nome_produto, preco, porcentagem):
    if porcentagem > 100:
        return "Você não pode dá um desconto maior que 100%"
    result = {
        "Nome do Produto": nome_produto,
        "Preço Original": f"R$ {preco}",
        "Porcentagem de desconto": f"{porcentagem}%",
        "Preço Final": f"R$ {preco - (preco * porcentagem / 100)}"

    }

    return result

if __name__ == "__main__":
    print(calcula_desconto("Iphone 15", 6000, 10))
