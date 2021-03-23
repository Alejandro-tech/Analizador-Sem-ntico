import re
from sys import flags
#####----INT ------ DOUBLE-----#####
#ESTRUCTURA REALES
#ACEPTADAS
estructuraU = r"(^int\s[a-z]+\s\=\s\d+\s[-*\/+]\s\d+\;$)|(^double\s\w+\s\=\s\d+\.\d+\s[-*/+]\s\d+\.\d+\;$)"  #int var|double = num op num;
estructuraD = r"(^int\s[a-z]+\s\=\s\d+\;$)|(^double\s\w+\s\=\s\d+\.\d+\;$)" #int|double var = num;
estructuraT = r"(^int\s[a-z]+\;)|(^double\s[a-z]+\;)" #int|double var;

#NO ACEPTADAS
estructuraNU = r"(^int\s\w+\s\=\s\"((\w+\s\w+){0,10})\"\;$)|(^int\s[a-z]+\s\=\s\d+\.\d+\;$)|(^int\s[a-z]+\s\=\s\"\d+\.\d+\"\;$)|(^int\s[a-z]+\s\=\s\d+\.\d+\s[-*/+]\s\d+\;$)"
estructuraND = r"(^double\s[a-z]+\s\=\s\d+\.\d+\s[-*/+]\s\d+\;$)|(^double\s\w+\s\=\s\"[a-z]+\"\;$)|(^int\s[a-z]+\;\n^[a-z]+\s\=\s\d+\.\d+\;$)"
estructuraNT = r"(^int\s[a-z]+\s\=\s\d+\s[-*/+]\s\d+\.\d+\;$)|(^int\s[a-z]+\;\n^[a-z]+\s\=\s\d+\s[-*/+]\s\d+\.\d+\;$)|(^int\s[a-z]+\;\n^[a-z]+\s\=\s\d+\.\d+\s[-*7+]\s\d+\;$)|(^int\s[a-z]+\s\=\s\d+\.\d+\s[-*/+]\s\d+\.\d+\;$)|(^int\s[a-z]+\s\=\s\"[a-z]+\"\;$)"
estructuraNC = r"(^double\s[a-z]+\;\n^\w+\s\=\s\d+\;$)|(^double\s[a-z]+\;\n^\w+\s\=\s\d+\s[-*/+]\s\d+\.\d+\;$)|(^double\s[a-z]+\;\n^\w+\s\=\s\d+\.\d+\s[-*/+]\s\d+\;$)"
estructuraNCin = r"(^int\s[a-z]+\s\=\s\d+\s[-*/+]\s\d+$)|(^int\s[a-z]+\s\=\s\d+$)|(int\s[a-z]+\n^[a-z]+\s\=\s\d+\s[-*/+]\s\d+$)|(int\s[a-z]+\n^[a-z]+\s\=\s\d+$)"
estructuraNS = r"(^double\s[a-z]+\s\=\s\d+\s[-*/+]\s\d+\.\d+\;$)|(^double\s\w+\s\=\s\"((\w+\s\w+){0,10})\"\;$)|(^double\s\w+\s\=\s\d+\;$)"
estructuraNSie = r"(int\s[a-z]+\;\n^[a-z]+\s\=\s\d+$)|(int\s[a-z]+\n^[a-z]+\s\=\s\d+\;$)|(int\s[a-z]+\;\n^[a-z]+\s\=\s\d+\s[-*/+]\s\d+$)|(int\s[a-z]+\n^[a-z]+\s\=\s\d+\s[-*/+]\s\d+\;$)"
estructuraNO = r"(^double\s[a-z]+\;\n^[a-z]+\s\=\s\d+\.\d+\s[-*/+]\s\d+\.\d+$)|(^double\s[a-z]+\n^[a-z]+\s\=\s\d+\.\d+\s[-*/+]\s\d+\.\d+\;$)"
estructuraNN = r"(^double\s[a-z]+\n^[a-z]+\s\=\s\d+\.\d+\s[-*/+]\s\d+\.\d+$)|(^double\s\w+\s\=\s\d+\.\d+\s[-*/+]\s\d+\.\d+$)|(^double\s[a-z]+\n^[a-z]+\s\=\s\d+\.\d+$)|(^double\s\w+\s\=\s\d+\.\d+$)"
#-----------------------------------------------------------------------------------------------------------------------------

#####--------STRING-----------#####
#ACEPTADAS
estructuraU1 = r"(string\s[a-z]+\s\=\s\"[a-z]+\"\;$)|(^string\s\w+\s\=\s\"((\w+\s\w+){1,10})\"\;$)|(^string\s\w+\;\n^[a-z]+\s\=\s\"((\w+\s\w+){0,10})\"\;$)|(^string\s\w+\;\n^[a-z]+\s\=\s\"((\w+\s\w+){0,10})\"\s[+]\s\"((\w+\s\w+){1,10})\"\;$)"
estructuraD1 = r"(string\s[a-z]+\;\n^[a-z]\s\=\s\"[a-z]\w+\"\s+[+]\s\"[a-z]\w+\"\;$)"
#NO ACEPTADAS
estructuraU11 = r"(string\s[a-z]+\;\n^[a-z]\s\=\s[0-9]\.[0-9]\;$)"
estructuraD11 = r"(^string\s\w+\s\=\s\"((\w+\s\w+){1,10})\"$)|(^string\s\w+\n^[a-z]+\s\=\s\"((\w+\s\w+){0,10})\"$)|(^string\s\w+\n^[a-z]+\s\=\s\"((\w+\s\w+){0,10})\"\s[+]\s\"((\w+\s\w+){1,10})\"$)|(^string\s\w+\s\=\s\"((\w+\s\w+){0,10})\"\s[+]\s\"((\w+\s\w+){1,10})\"$)"

#####--------BOOLEAN----------#####
# ACEPTADAS
estructuraU2 = r"(^boolean\s[a-zA-Z]+\;\n^[a-zA-Z]\s+=\s[0-9]\s[<>]\s[0-9]\;$)"
estructuraD2 = r"(^boolean\s\w+\s\=\strue\;$)|(^boolean\s\w+\;\n^[a-z]+\s\=\strue\;$)|(^boolean\s\w+\;\n^[a-z]+\s\=\s\d+\s(<|>|<=|>=)\s\d+\;$)"

# NO ACEPTADAS
estructuraU22 = r"(^boolean\s[a-zA-Z]\;\n[a-zA-Z]\s+=\s[0-9]\s[+*^-]\s[0-9]\;$)"
estructuraD22 = r" (^boolean\s\w+\s\=\strue$)|(^boolean\s\w+\s\=\s\d+\s(<|>|<=|>=)\s\d+$)|(^boolean\s\w+\s\=\s\d+\;$)|(^boolean\s[a-z]+\;\n^\w+\s\=\s\d+\;$)|(^boolean\s[a-z]+\;\n\w+\s\=\s\d+\.\d+\;$)"

#####-------------FLOAT-------------###########
# ACEPTADA
estructuraU3 = r"(^float\s\w+\s\=\s\d+\.\d+\;$)|(^float\s\w+\s\=\s\d+\.\d+\s[+/*-]\s\d+\.\d+\;$)|(^float\s\w+\;\n^[a-z]+\s\=\s\d+\.\d+\;$)|(^float\s\w+\;\n^[a-z]+\s\=\s\d+\.\d+\s[+/*-]\s\d+\.\d+\;$)"

# NO ACEPTADA
estructuraU33 = r"(float\s[a-z]\n[a-zA-Z]\s+=\s\"[0-9]\.[0-9]\"\;$)"
estructuraD33 = r"(^float\s\w+\s\=\s\d+\;$)|(^float\s[a-z]\;\n^\w+\s\=\s\d+\;$)|(^float\s\w+\s\=\s\d+\.\d+\s[-*/+]\s\d+\;$)|(^float\s\w+\s\=\s\d+\s[-*/+]\s\d+\.\d+\;$)|(^float\s\w+\s\=\s\d+\s[-*/+]\s\d+\.\d+\;$)"

dir = r"C:\Users\Antonio Caamal\OneDrive\Documentos\lineas.txt"

f = open(dir, "r")
linea = f.read()
print(linea)

#SinErrorU = len(re.findall(estructuraU,estructuraD,estructuraT, linea, re.MULTILINE))
#if coincidencias1 >= 1:
#    print("Sin Errores")
SinErroresU = len(re.findall(estructuraU, linea, re.MULTILINE))
if SinErroresU >= 1:
    print("ÉXITO EN EJECUCIÓN")

SinErroresD = len(re.findall(estructuraD, linea, re.MULTILINE))
if SinErroresD >= 1:
    print("ÉXITO EN EJECUCIÓN")

SinErroresT = len(re.findall(estructuraT, linea, re.MULTILINE))
if SinErroresT >= 1:
    print("ÉXITO EN EJECUCIÓN")

ConErrorU = len(re.findall(estructuraNU, linea, re.MULTILINE))
if ConErrorU >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorD = len(re.findall(estructuraND, linea, re.MULTILINE))
if ConErrorD >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorT = len(re.findall(estructuraNT, linea, re.MULTILINE))
if ConErrorT >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorCu = len(re.findall(estructuraNC, linea, re.MULTILINE))
if ConErrorCu >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorCi = len(re.findall(estructuraNCin, linea, re.MULTILINE))
if ConErrorCi >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorS = len(re.findall(estructuraNS, linea, re.MULTILINE))
if ConErrorS >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorSi = len(re.findall(estructuraNSie, linea, re.MULTILINE))
if ConErrorSi >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorO = len(re.findall(estructuraNO, linea, re.MULTILINE))
if ConErrorO >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorN = len(re.findall(estructuraNN, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (INT/DOUBLE)")

ConErrorN = len(re.findall(estructuraU1, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("ÉXITO EN EJECUCION")

ConErrorN = len(re.findall(estructuraU11, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (STRING)")

ConErrorN = len(re.findall(estructuraD1, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("ÉXITO EN EJECUCION")

ConErrorN = len(re.findall(estructuraD11, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (STRING)")

ConErrorN = len(re.findall(estructuraU2, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("ÉXITO EN EJECUCION")

ConErrorN = len(re.findall(estructuraD2, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("ÉXITO EN EJECUCION")

ConErrorN = len(re.findall(estructuraU22, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (BOOLEAN)")

ConErrorN = len(re.findall(estructuraD22, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (BOOLEAN)")

ConErrorN = len(re.findall(estructuraU3, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("ÉXITO EN EJECUCION")

ConErrorN = len(re.findall(estructuraU33, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (FLOAT)")

ConErrorN = len(re.findall(estructuraD33, linea, re.MULTILINE))
if ConErrorN >= 1:
    print("SIN ÉXITO, EXISTE UN ERROR TIPO (FLOAT)")