from enum import Enum

class Tag(Enum):
    # Fim de arquivo
    EOF = -1

    # Palavras-chave
    KW_IF = 1
    KW_ELSE = 2
    KW_PRINT = 4
    KW_NUM = 5
    KW_CHAR = 6
    KW_OR = 7
    KW_AND = 8
    KW_NOT = 9
    KW_WRITE = 10
    KW_WHILE = 11
    KW_PROGRAM = 12
    KW_READ = 13

    # Operadores
    OP_MENOR = 14  # <
    OP_MENOR_IGUAL = 15  # <=
    OP_MAIOR_IGUAL = 16  # >=
    OP_MAIOR = 17  # >
    OP_IGUAL = 18  # =
    OP_NAO_IGUAL = 19  # !=
    OP_DIVISAO = 20  # /
    OP_MULTIPLICACAO = 21  # *
    OP_SOMA = 22  # +
    OP_SUBTRACAO = 23  # -
    OP_IGUAL_IGUAL = 24  # ==

    # Simbolos
    SMB_PONTO_VIRGULA = 25  # ;
    SMB_ABRE_PAREN = 26  # (
    SMB_FECHA_PAREN = 27  # )
    SMB_VIRGULA = 28  # ,
    SMB_ABRE_CHAVE = 29  # {
    SMB_FECHA_CHAVE = 30  # }

    # Identificador
    ID = 31
    LIT = 32

    # Numeros
    NUM = 33
    NUM_CONST = 34
    CHAR_CONST = 35