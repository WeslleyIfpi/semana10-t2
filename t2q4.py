def cancaoPop():
    saida = ''
    frase = ' bugs no software, pegue um deles e conserte... '
    for i in range(99, 10, -11):
        saida += str(i)
        saida += frase
        print(saida)
        print('Tecle "Ctrl+F5"')
        saida = ''
    print('Sem erros no software! Está estabilizado!')

def main():
    cancaoPop()

if __name__ == '__main__':
    main()