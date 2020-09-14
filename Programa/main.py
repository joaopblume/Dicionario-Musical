def AcMenor():
    i = escala.index(acorde[0])
    indices = [i, (i + 3) % len(escala), (i + 7) % len(escala)]

    if '#' in acorde or 'b' in acorde:
        i = escala.index(acorde[0:2])
        indices = [i, (i + 3) % len(escala), (i + 7) % len(escala)]

    triade = [escala[idx] for idx in indices]
    x = f'A fundamental é \033[1;94m{triade[0]}\033[m, ' \
        f'a terça é \033[1;94m{triade[1]}\033[m e a quinta é \033[1;94m{triade[2]}\033[m.'
    print('=' * 50)
    print(x.center(50))
    print('=' * 50)


def AcMaior():
    i = escala.index(acorde[0])
    indices = [i, (i + 4) % len(escala), (i + 7) % len(escala)]

    if '#' in acorde or 'b' in acorde:
        i = escala.index(acorde[0:2])
        indices = [i, (i + 4) % len(escala), (i + 7) % len(escala)]

    triade = [escala[idx] for idx in indices]
    x = f'A fundamental é \033[1;32m{triade[0]}\033[m, ' \
        f'a terça é \033[1;32m{triade[1]}\033[m e a quinta é \033[1;32m{triade[2]}\033[m.'
    print('=' * 50)
    print(x.center(50))
    print('=' * 50)


def Setima():
    i = (escala.index(acorde[0]) + 10) % len(escala)
    seti = escala[i]

    if '#' in acorde or 'b' in acorde:
        i = (escala.index(acorde[0:2]) + 10) % len(escala)
        seti = escala[i]
    s = f'Sua sétima é \033[1;35m{seti}\033[m.'
    print('=' * 50)
    print(s.center(50))
    print('=' * 50)


k = 'Dicionário Musical'
print('=' * 50)
print(k.center(50))
print('=' * 50)

notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notasbemol = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
escala = notas[:]

acorde = str(input('Acorde desejado: ')).replace('M', 'm')

while True:
    if 'b' in acorde:
        escala = notasbemol[:]

    if '#' in acorde or 'b' in acorde:
        if acorde[0:2] not in escala:
            print(f"\033[31mAcorde inválido, por favor digite um acorde existente.\033[m")
            acorde = str(input('Acorde desejado: '))
        else:
            break

    elif acorde[0] not in escala:
        print(f"\033[31mAcorde inválido, por favor digite um acorde existente.\033[m")
        acorde = str(input('Acorde desejado: '))

    else:
        break

if 'm' in acorde:  # se um acorde menor
    AcMenor()

else:  # se for um acorde maior
    AcMaior()

setima = input('Deseja saber a sétima do acorde? [S/N] ').upper()
while True:
    if setima not in 'SN':
        print('\033[31mResposta inválida, digite apenas S ou N;\033[m')
        setima = input('Deseja saber a sétima do acorde? [S/N]').upper()
    else:
        break

if setima == 'S':
    Setima()
