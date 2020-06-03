import ply.lex as lex
from ply.lex import TOKEN
tokens=(
    'numero', #Este token tendra un metodo def
    'signoMas', #Este token no tendra metodo def, solo se declarara como t_, por lo que al encontrarlo el analizador, este dira que es un signo mas
);
t_signoMas=r'\+';
#t_numero=r'\d+'; #borra el metodo def y activa este, hara los mismo
def t_numero(t):
    r'\d+' #Aqui esta la gramatica de un numero
    t.value = int(t.value)
    return t

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1) #Aqui le decimos cuantos caracteres queremos que omita despues del error

#creamos el lexer
lexer = lex.lex()
data="123123 +"
#Le damos como argumento los datos del archivo
lexer.input(data)

 # El token analiza cada linea en cada iteracion
while True:
    tok = lexer.token() #El token tiene metodos definidos, si encuentra uno que coincida con fecha, entonces imprimira que es un token
    if not tok:
        break
    print(tok)
