import ply.lex as lex
from ply.lex import TOKEN
tokens=(
    'fecha',
    'mes',
    'anio',
    'dia',
    'digito',
    'digitoMes',
    'digitoDia'

);
#DEFINIMOS LA GRAMATICA
digito=r'([0-9])';
digitoMes=r'([0-1])'; #primer digito del mes debe ser 0 o 1
digitoDia=r'([0-3])';#primer digito del dia debe ser 0 o 3

dia=digitoDia+digito;
mes=digitoMes+digito;
anio=digito+digito+digito+digito; # no restringimos el año de inicio
fecha=anio+mes+dia;

@TOKEN(fecha) #Utilizamos el @token para combinar las gramaticas antes definidas
def t_fecha(t):
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1) #Aqui le decimos cuantos caracteres queremos que omita despues del error

#le decimos que ignore el salto de linea
t_ignore  = ' \n'

#creamos el lexer
lexer = lex.lex()

#abrimos el archivo
f = open("entrada.txt",'r')
data = f.read() #Guardamos el contenido del archivo en una variable
f.close()

#Le damos como argumento los datos del archivo
lexer.input(data)

 # El token analiza cada linea en cada iteracion
while True:
    tok = lexer.token() #El token tiene metodos definidos, si encuentra uno que coincida con fecha, entonces imprimira que es un token
    if not tok:
        break
    print(tok)
