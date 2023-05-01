def cancaoPop():
    saida = ''
    frase = ' bugs no software, pegue um deles e conserte... '
    for i in range(99, 251):
        saida += str(i)
        saida += frase
        print(saida)
        saida = ''

def main():
    cancaoPop()

if __name__ == '__main__':
    main()