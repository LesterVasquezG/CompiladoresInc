import ply.lex as lex
import re
from ply.lex import TOKEN

fuente = open("fuente.txt", "r")
salida = open("salida.txt", "w")

fechasFuente = fuente.read()
fechas = set(fechasFuente.split('\n'))
fechasValidas = set(fechas.copy())
fechasInvalidas = set(fechas.copy())

tokens=(
    'fecha',
    'mes',
    'anio',
    'dia',
    'digito',
    'digitoMes',
    'digitoDia'
)

# Definimos la gramatica
digito = r'([0-9])'
digitoMes = r'([0-1])'  # Primer digito del mes debe ser 0 o 1
digitoDia = r'([0-3])'  # Primer digito del dia debe ser 0 o 3

dia = digitoDia + digito
mes = digitoMes + digito
anio = digito + digito + digito + digito # No restringimos el año de inicio
fecha = anio + mes + dia

# Utilizamos el @token para combinar las gramaticas antes definidas
@TOKEN(fecha)

def t_fecha(t):
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    #print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1) #Aqui le decimos cuantos caracteres queremos que omita despues del error

# Ignorar el salto de linea
t_ignore  = ' \n'

# Creamos el lexer
lexer = lex.lex()

# Entrada: datos del archivo
lexer.input(fechasFuente)

 # El token analiza cada linea en cada iteracion
while True:
    # El token tiene metodos definidos, si encuentra uno que coincida con fecha, entonces imprimira que es un token
    tok = lexer.token()
    if not tok:
        break
    else:
        fechasInvalidas.remove(str(tok.value))

# Impresion en consola de las fechas/tokens incorrectos
fechasIncorrectas = ""
for i in fechasInvalidas:
    fechasIncorrectas += i + ", "
print("Las fechas " + fechasIncorrectas + "son incorrectas")

# Fechas validas en archivo salida ---> Fechas validas = Fechas - Fechas invalidas
fechasValidas = fechas - fechasInvalidas

for fecha in fechasValidas:

    componentes = []
    while fecha:
        componentes.append(fecha[:2])
        fecha = fecha[2:]


    salida.write(componentes[0] + componentes[1] + "/" + componentes[2] + "/" + componentes[3] + "\n")

fuente.close()
salida.close()
