from tag import Tag
from token import Token

class TS:
    # dicionario: {"chave" : "valor"}
    def __init__(self):
        self.ts = {}

        # Palavras-chave
        self.ts['if'] = Token(Tag.KW_IF, 'if', 0, 0)
        self.ts['else'] = Token(Tag.KW_ELSE, 'else', 0, 0)
        self.ts['print'] = Token(Tag.KW_PRINT, 'print', 0, 0)
        self.ts['while'] = Token(Tag.KW_WHILE, 'while', 0, 0)
        self.ts['write'] = Token(Tag.KW_WRITE, 'write', 0, 0)
        self.ts['read'] = Token(Tag.KW_READ, 'read', 0, 0)
        self.ts['num'] = Token(Tag.KW_NUM, 'num', 0, 0)
        self.ts['char'] = Token(Tag.KW_CHAR, 'char', 0, 0)
        self.ts['not'] = Token(Tag.KW_NOT, 'not', 0, 0)
        self.ts['or'] = Token(Tag.KW_OR, 'or', 0, 0)
        self.ts['and'] = Token(Tag.KW_AND, 'and', 0, 0)
        self.ts['program'] = Token(Tag.KW_PROGRAM, 'program', 0, 0)

        # Operadores
        self.ts['=='] = Token(Tag.OP_IGUAL_IGUAL, '==', 0, 0)
        self.ts['!='] = Token(Tag.OP_NAO_IGUAL, '!=', 0, 0)
        self.ts['>'] = Token(Tag.OP_MAIOR, '>', 0, 0)
        self.ts['<'] = Token(Tag.OP_MENOR, '<', 0, 0)
        self.ts['>='] = Token(Tag.OP_MAIOR_IGUAL, '>=', 0, 0)
        self.ts['<='] = Token(Tag.OP_MENOR_IGUAL, '<=', 0, 0)
        self.ts['+'] = Token(Tag.OP_SOMA, '+', 0, 0)
        self.ts['-'] = Token(Tag.OP_SUBTRACAO, '-', 0, 0)
        self.ts['*'] = Token(Tag.OP_MULTIPLICACAO, '*', 0, 0)
        self.ts['/'] = Token(Tag.OP_DIVISAO, '/', 0, 0)
        self.ts['='] = Token(Tag.OP_IGUAL, '=', 0, 0)

        # Operadores
        self.ts['{'] = Token(Tag.SMB_ABRE_CHAVE, '{', 0, 0)
        self.ts['}'] = Token(Tag.SMB_FECHA_CHAVE, '}', 0, 0)
        self.ts['('] = Token(Tag.SMB_ABRE_PAREN, '(', 0, 0)
        self.ts[')'] = Token(Tag.SMB_FECHA_PAREN, ')', 0, 0)
        self.ts[','] = Token(Tag.SMB_VIRGULA, ',', 0, 0)
        self.ts[';'] = Token(Tag.SMB_PONTO_VIRGULA, ';', 0, 0)

        # Identificador
        self.ts['id'] = Token(Tag.ID, 'id', 0, 0)
        self.ts['lit'] = Token(Tag.LIT, 'lit', 0, 0)

        # Numeros
        self.ts['num'] = Token(Tag.NUM, 'num', 0, 0)
        self.ts['num_const'] = Token(Tag.NUM_CONST, 'num_const', 0, 0)
        self.ts['char_const'] = Token(Tag.CHAR_CONST, 'char_const', 0, 0)

    def getToken(self, lexema):
        token = self.ts.get(lexema)
        return token

    def addToken(self, lexema, token):
        self.ts[lexema] = token

    def printTS(self):
        for k, t in (self.ts.items()):
            print(k, ":", t.toString())
