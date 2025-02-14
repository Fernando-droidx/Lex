import ply.lex as lex

# Lista de tokens
tokens = [
    'IDENTIFIER', 'INTEGER', 'FLOAT', 'FLOAT_KEYWORD', 'STRING',  # Identificadores y literales
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',  # Operadores aritméticos
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',  # Operadores relacionales
    'ASSIGN',  # Operador de asignación
    'AND', 'OR', 'NOT',  # Operadores lógicos
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',  # Paréntesis, llaves y corchetes
    'COMMA', 'SEMICOLON', 'DOT'  # Otros símbolos
]

# Palabras clave del lenguaje C
reserved = {
    'auto': 'AUTO', 'break': 'BREAK', 'case': 'CASE', 'char': 'CHAR',
    'const': 'CONST', 'continue': 'CONTINUE', 'default': 'DEFAULT', 'do': 'DO',
    'double': 'DOUBLE', 'else': 'ELSE', 'enum': 'ENUM', 'extern': 'EXTERN',
    'float': 'FLOAT', 'for': 'FOR', 'goto': 'GOTO', 'if': 'IF', 'int': 'INT',
    'long': 'LONG', 'register': 'REGISTER', 'return': 'RETURN', 'short': 'SHORT',
    'signed': 'SIGNED', 'sizeof': 'SIZEOF', 'static': 'STATIC', 'struct': 'STRUCT',
    'switch': 'SWITCH', 'typedef': 'TYPEDEF', 'union': 'UNION', 'unsigned': 'UNSIGNED',
    'void': 'VOID', 'volatile': 'VOLATILE', 'while': 'WHILE'
}

# Agregar las palabras clave como tokens
tokens += list(reserved.values())

# Reglas para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_ASSIGN = r'='

t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

t_COMMA = r','
t_SEMICOLON = r';'
t_DOT = r'\.'

# Reglas complejas
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verificar si es palabra clave
    return t

def t_INVALID_FLOAT(t):
    r'\d+\.$'
    print(
        f"[Error Léxico] Literal numérico flotante mal formado '{t.value}' en la línea {t.lineno}, columna {t.lexpos}")
    t.lexer.skip(len(t.value))  # Ignorar el token completo

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_UNTERMINATED_STRING(t):
    r'"([^"\\]|\\.)*'
    print(f"[Error Léxico] Cadena mal formada en la línea {t.lineno}, columna {t.lexpos}: No se cerraron las comillas.")
    t.lexer.skip(len(t.value))  # Ignorar la cadena

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remover comillas
    return t

# Comentarios
def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    pass

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)



# Construir el lexer
lexer = lex.lex()
