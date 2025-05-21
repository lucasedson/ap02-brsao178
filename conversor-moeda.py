def conversor(valor, moeda:str):
    '''
    Função que converte Real -> Dólar ou Real -> Euro.
    Use: 'USD' para dolar ou 'EUR' para euro
    '''
    moeda = moeda.upper()
    if moeda == 'USD':
        result = float(valor) * 5.20
        return f'U$ {result:.2f}'
    elif moeda == 'EUR':
        return f'€ {valor * 6.15:.2f}'
    else:
        return 'Moeda inválida'


if __name__ == '__main__':
    print(conversor(1, 'USD'))    
    print(conversor(2.5, 'USD'))    
    print(conversor(0, 'USD'))    
    print(conversor(1, 'eur'))