import sys

from ts import TS
from tag import Tag
from token import Token

class Lexer:
    '''
    Classe que representa o Lexer (AFD):

    [1] Voce devera se preocupar quando incremetar as linhas e colunas,
    assim como, quando decrementar ou reinicia-las. Lembre-se, ambas
    comecam em 1.
    [2] Toda vez que voce encontrar um lexema completo, voce deve retornar
    um objeto Token(Tag, "lexema", linha, coluna). Cuidado com as
    palavras reservadas, que ja sao cadastradas na TS. Essa consulta
    voce devera fazer somente quando encontrar um Identificador.
    [3] Se o caractere lido nao casar com nenhum caractere esperado,
    apresentar a mensagem de erro na linha e coluna correspondente.
    Obs.: lembre-se de usar o metodo retornaPonteiro() quando necessario.
          lembre-se de usar o metodo sinalizaErroLexico() para mostrar
          a ocorrencia de um erro lexico.
    '''
    def __init__(self, input_file):
        try:
            self.input_file = open(input_file, 'rb')
            self.lookahead = 0
            self.n_line = 1
            self.n_column = 0
            self.ts = TS()
            self.erros = 0
        except IOError:
            print('Erro de abertura do arquivo. Encerrando.')
            sys.exit(0)

    def closeFile(self):
        try:
            self.input_file.close()
        except IOError:
            print('Erro ao fechar arquivo. Encerrando.')
            sys.exit(0)

    def sinalizaErroLexico(self, message):
        self.erros = self.erros + 1
        print("[Erro Lexico]: ", message, "\n")

    def retornaPonteiro(self):
        if self.lookahead.decode('ascii') != '':
            self.input_file.seek(self.input_file.tell() - 1)
        self.n_column = self.n_column - 1

    def printTS(self):
        self.ts.printTS()

    def proxToken(self):
        estado = 1
        lexema = ""
        c = '\u0000'

        while (True):
            self.lookahead = self.input_file.read(1)
            c = self.lookahead.decode('ascii').lower()

            self.n_column = self.n_column + 1

            if (c == "\n"):
                self.n_column = 0

            if (estado == 1):
                if (c == ''):
                    return Token(Tag.EOF, "EOF", self.n_line, self.n_column)
                elif (c == ' ' or c == '\t' or c == '\n' or c == '\r'):
                    estado = 1
                    if (c == '\n'):
                        self.n_line = self.n_line + 1
                elif (c == '='):
                    estado = 2
                elif (c == '!'):
                    estado = 4
                elif (c == '<'):
                    estado = 6
                elif (c == '>'):
                    estado = 9
                elif (c.isdigit()):
                    lexema += c
                    estado = 12
                elif (c.isalpha()):
                    lexema += c
                    estado = 14
                elif (c == '{'):
                    return Token(Tag.SMB_ABRE_CHAVE, "{", self.n_line, self.n_column)
                elif (c == '}'):
                    return Token(Tag.SMB_FECHA_CHAVE, "}", self.n_line, self.n_column)
                elif (c == '('):
                    return Token(Tag.SMB_ABRE_PAREN, "(", self.n_line, self.n_column)
                elif (c == ')'):
                    return Token(Tag.SMB_FECHA_PAREN, ")", self.n_line, self.n_column)
                elif (c == '/'):
                    estado = 18
                elif (c == '-'):
                    return Token(Tag.OP_MENOR, "-", self.n_line, self.n_column)
                elif (c == '+'):
                    return Token(Tag.OP_SOMA, "+", self.n_line, self.n_column)
                elif (c == '*'):
                    return Token(Tag.OP_MULTIPLICACAO, "*", self.n_line, self.n_column)
                elif (c == ';'):
                    return Token(Tag.SMB_PONTO_VIRGULA, ";", self.n_line, self.n_column)
                elif (c == ','):
                    return Token(Tag.SMB_VIRGULA, ",", self.n_line, self.n_column)
                elif (c == '"'):
                    estado = 16
                else:
                    lexema += c
                    self.sinalizaErroLexico("Caractere invalido [" + c + "] na linha " + str(self.n_line) + " e coluna " + str(self.n_column))
                    if (self.erros == 3):
                        return None
                    else:
                        return ''

            elif (estado == 2):
                if (c == '='):
                    return Token(Tag.OP_IGUAL_IGUAL, "==", self.n_line, self.n_column)
                else:
                    self.retornaPonteiro()
                    return Token(Tag.OP_IGUAL, "=", self.n_line, self.n_column)

            elif (estado == 4):
                if (c == '='):
                    return Token(Tag.OP_NAO_IGUAL, "!=", self.n_line, self.n_column)

                self.sinalizaErroLexico("Caractere invalido [" + c + "] na linha " + str(self.n_line) + " e coluna " + str(self.n_column))
                self.retornaPonteiro()

                if (self.erros == 3):
                    return None
                else:
                    return ''

            elif (estado == 6):
                if c == '=':
                    return Token(Tag.OP_MENOR_IGUAL, "<=", self.n_line, self.n_column)

                self.retornaPonteiro()
                return Token(Tag.OP_MENOR, "<", self.n_line, self.n_column)

            elif (estado == 9):
                if c == '=':
                    return Token(Tag.OP_MAIOR_IGUAL, ">=", self.n_line, self.n_column)

                self.retornaPonteiro()
                return Token(Tag.OP_MAIOR, ">", self.n_line, self.n_column)

            elif (estado == 12):
                if (c.isdigit()):
                    lexema += c
                if (c == '.'):
                    lexema += c
                    estado = 19
                else:
                    self.retornaPonteiro()
                    return Token(Tag.NUM, lexema, self.n_line, self.n_column)

            elif (estado == 14):
                if (c.isalnum()):
                    lexema += c
                else:
                    self.retornaPonteiro()
                    token = self.ts.getToken(lexema)

                    if (token is None):
                        token = Token(Tag.ID, lexema, self.n_line, self.n_column)
                        self.ts.addToken(lexema, token)
                    else:
                        token = Token(Tag.ID, lexema, self.n_line, self.n_column)
                        self.ts.udpatePosition(lexema, token)

                    return token

            elif (estado == 15):
                if (c == '\n'):
                    self.n_line = self.n_line + 1
                elif (c == '*'):
                    estado = 17
                elif (c == ''):
                    return Token(Tag.EOF, "EOF", self.n_line, self.n_column - 1)

            elif (estado == 16):
                if (c == '"'):
                    return Token(Tag.CHAR_CONST, lexema, self.n_line, self.n_column)
                elif (c == ''):
                    coluna = self.n_column
                    self.n_column = 0
                    return Token(Tag.CHAR_CONST, lexema, self.n_line, coluna)
                elif (c == '\n'):
                    self.sinalizaErroLexico("Quebra de linha inválida na linha " + str(self.n_line) + " e coluna " + str(self.n_column))
                    self.retornaPonteiro()

                    if (self.erros == 3):
                        return None
                    else:
                        return ''
                lexema += c

            elif (estado == 17):
                if (c == '/'):
                    estado = 1
                else:
                    estado = 15

            elif (estado == 18):
                if (c == '*'):
                    estado = 15
                elif (c == '/'):
                    estado = 20
                else:
                    self.retornaPonteiro()
                    return Token(Tag.OP_DIVISAO, '/', self.n_line, self.n_column)

            elif (estado == 19):
                if (c.isdigit()):
                    lexema += c
                else:
                    self.retornaPonteiro()
                    return Token(Tag.NUM_CONST, lexema, self.n_line, self.n_column)
                    
            elif (estado == 20):
                if (c == ''):
                    return Token(Tag.EOF, "EOF", self.n_line, self.n_column)
                elif (c == '\n'):
                    self.n_line = self.n_line + 1
                    estado = 1
            # fim if's de estados
        # fim while
