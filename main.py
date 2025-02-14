from lexer import lexer

def main():
    with open('tests/errors.c', 'r') as f:
        code = f.read()
    lexer.input(code)


    print("Tokens y errores encontrados:")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
if __name__ == '__main__':
    main()
