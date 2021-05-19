from tag import Tag
from token import Token
from lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer('prog1.txt')

    print("\nLista de tokens:\n")
    token = lexer.proxToken()
  ##### MUDARRRRRRR
    if token.getNome() != Tag.EOF:
        print("Teste")
        print(token.toString(), "Linha: " + str(token.getLinha()) + " Coluna: " + str(token.getColuna()))
    else:
        print("Teste2")
        while token is not None:
            if token == False:
                token = lexer.proxToken()
                continue
        print(token.toString(), "Linha: " + str(token.getLinha()) + " Coluna: " + str(token.getColuna()))
        token = lexer.proxToken()
    ##### FIM MUDARRRRRRR
    print("\nTabela de simbolos:\n")
    lexer.printTS()
    lexer.closeFile()
    print('\nFim da compilacao\n')
