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
    'digitoDia',
    'hora',
    'espacio'
)

# Definimos la gramatica
espacio=r'(\s)'#detecta el espacio
digito = r'([0-9])'
digitoMes = r'([0-1])'  # Primer digito del mes debe ser 0 o 1
digitoDia = r'([0-3])'  # Primer digito del dia debe ser 0 o 3

dia = digitoDia + digito
mes = digitoMes + digito
anio = digito + digito + digito + digito # No restringimos el año de inicio
hora=digito+digito+digito+digito
fecha = anio + mes + dia+ espacio+ hora

# Utilizamos el @token para combinar las gramaticas antes definidas
@TOKEN(fecha)
def t_fecha(t):
    t.value = str(t.value)
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
print("Las fechas y/u horas " + fechasIncorrectas + "son incorrectas")

# Fechas y horas validas en archivo salida ---> Fechas validas = Fechas - Fechas invalidas
fechasValidas = fechas - fechasInvalidas

for fechaCompleta in fechasValidas:

    fecha = fechaCompleta.split(" ")[0]
    hora = fechaCompleta.split(" ")[1]

    componentes = [fecha[0:2], fecha[2:4], fecha[4:6]]
    texto = componentes[0] + "/" + componentes[1] + "/" + componentes[2] + " "

    componentes = [hora[0:2], hora[2:4]]
    texto += componentes[0] + ":" + componentes[1] + "\n"

    salida.write(texto)

fuente.close()
salida.close()