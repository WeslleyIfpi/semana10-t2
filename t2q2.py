def cancaoPop():
    saida = ''
    frase = ' bugs no software, pegue um deles e conserte... '
    for i in range(99, 251):
        saida += str(i)
        saida += frase
        print(saida)
        print('Tecle "Ctrl+F5"')
        saida = ''
    print('Vamos fazer mais um café!')

def main():
    cancaoPop()

if __name__ == '__main__':
    main()