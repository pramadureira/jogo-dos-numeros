cartao1 = ((1, 3, 5, 7),
           (9, 11, 13, 15),
           (17, 19, 21, 23),
           (25, 27, 29, 31),
           (33, 35, 37, 39),
           (41, 43, 45, 47),
           (49, 51, 53, 55),
           (57, 59, 61, 63))
cartao2 = ((2, 3, 6, 7),
           (10, 11, 14, 15),
           (18, 19, 22, 23),
           (26, 27, 30, 31),
           (34, 35, 38, 39),
           (42, 43, 46, 47),
           (50, 51, 54, 55),
           (58, 59, 62, 63))
cartao3 = ((4, 5, 6, 7),
           (12, 13, 14, 15),
           (20, 21, 22, 23),
           (28, 29, 30, 31),
           (36, 37, 38, 39),
           (44, 45, 46, 47),
           (52, 53, 54, 55),
           (60, 61, 62, 63))
cartao4 = ((8, 9, 10, 11),
           (12, 13, 14, 15),
           (24, 25, 26, 27),
           (28, 29, 30, 31),
           (40, 41, 42, 43),
           (44, 45, 46, 47),
           (56, 57, 58, 59),
           (60, 61, 62, 63))
cartao5 = ((16, 17, 18, 19),
           (20, 21, 22, 23),
           (24, 25, 26, 27),
           (28, 29, 30, 31),
           (48, 49, 50, 51),
           (52, 53, 54, 55),
           (56, 57, 58, 59),
           (60, 61, 62, 63))
cartao6 = ((32, 33, 34, 35),
           (36, 37, 38, 39),
           (40, 41, 42, 43),
           (44, 45, 46, 47),
           (48, 49, 50, 51),
           (52, 53, 54, 55),
           (56, 57, 58, 59),
           (60, 61, 62, 63))

cartoes = (cartao1, cartao2, cartao3, cartao4, cartao5, cartao6)

tapete = [['01', '02', '03', '04', '05', '06', '07', '08', '09'],
          ['10', '11', '12', '13', '14', '15', '16', '17', '18'],
          ['19', '20', '21', '22', '23', '24', '25', '26', '27'],
          ['28', '29', '30', '31', '32', '33', '34', '35', '36'],
          ['37', '38', '39', '40', '41', '42', '43', '44', '45'],
          ['46', '47', '48', '49', '50', '51', '52', '53', '54'],
          ['55', '56', '57', '58', '59', '60', '61', '62', '63']]


def procurador(numero):
    linha = coluna = 0
    for lin, lista_linha in enumerate(tapete):
        for col, num in enumerate(lista_linha):
            if int(num) == numero:
                linha = lin
                coluna = col
    return [coluna, linha]


def adivinha():
    # Mostra os cartões ao usuário e pergunta se o número está lá e retorna o número escolhido
    certo = 0
    for n, cartao in enumerate(cartoes):
        print(f'Cartão {n+1}')
        for linha in cartao:
            for numero in linha:
                print(f'{numero:^4}', end='')
            print()
        while True:
            resp = str(input(f'O número escolhido está no cartao {n+1}? [S/N] ')).upper().strip()
            if resp in 'SIMNAONÃO':
                break
            else:
                print('ERRO! Digite novamente!')
        print()
        if resp in 'SIM':
            certo += cartao[0][0]
    return certo


def mostrartapete():
    for linha in tapete:
        for numero in linha:
            print(f'{numero:^4}', end='')
        print()
    print()


def robot():
    from time import sleep
    linha = 0
    while True:
        while True:
            try:
                comeco = int(input('Número para começar: '))
            except Exception:
                print('ERRO! Digite novamente!')
            else:
                break
        if 1 <= comeco <= 63:
            pos_ni = procurador(comeco)
            break
        else:
            print('ERRO! Digite um número entre 1 e 63!')
    li = pos_ni[1]
    ci = pos_ni[0]
    if ci <= posicao[0]:
        passocol = 1
        limcol = posicao[0]+1
    else:
        passocol = -1
        limcol = posicao[0] - 1
    if li <= posicao[1]:
        passolin = 1
        limlin = posicao[1] + 1
    else:
        passolin = -1
        limlin = posicao[1] - 1

    for linha in range(li, limlin, passolin):
        temp = tapete[linha][ci]
        tapete[linha][ci] = 'XX'
        mostrartapete()
        tapete[linha][ci] = temp
        sleep(0.8)
    if ci <= posicao[0]:
        ci += 1
    else:
        ci -= 1

    for coluna in range(ci, limcol, passocol):
        temp = tapete[linha][coluna]
        tapete[linha][coluna] = 'XX'
        mostrartapete()
        tapete[linha][coluna] = temp
        sleep(0.8)

numCerto = adivinha()
posicao = procurador(numCerto)
robot()
print(f'O número escolhido foi o {numCerto}')
