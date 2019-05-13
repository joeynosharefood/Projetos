p = [0, 0, 0]
print(len(p))
c = 0
while True:
    p[c] = int(input('Insira um número: '))
    x = str(input('Deseja continuar ? '))
    if x in 'Nn':
        break
    c += 1
    print(p)
    print(c)
    if c >= len(p):
        while True:
            p.append(int(input('Insira um número: ')))
            x = str(input('Deseja continuar ? '))
            if x in 'Nn':
                break
            print(p)
            c += 1
            print(c)
        break
print(p)