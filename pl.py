def lexer(filecontents):
    token = ""
    state = 0
    for char in filecontents:
        token += char
        if token == " ":
            token = ""
        elif token == "PRINT"
def lang(filename):