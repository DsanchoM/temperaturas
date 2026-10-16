
print("\n---------INFORME DE TEMPERATURAS-----------")

temperaturas=[18.5, 21.2, 19.8, 23.1, 25.4]
umbral_calor=20
print("El registro de temperaturas es el siguiente: ", temperaturas)

# --------FUNCIONES----------
def calcular_media(lista):
    return sum(lista)/len(lista)

def calcular_maxima(lista):
    return max(lista)

def calcular_minima(lista):
    return min(lista)

def contar_temp_altas(lista, umbral):
    contador=0

    for t in lista:
       if t>20:
         contador=contador+1
    return contador

def hay_alerta(lista, umbral):
    for t in lista:
        if t>umbral:
            return True
    return False

def clasificar_temperaturas(t):
    if t<20:
        return "frío"
    elif t<=25:
        return "templado"
    else:
        return "calor"

def resumen_temperaturas(lista):
    resumen=[]
    for t in lista:
        etiqueta=clasificar_temperaturas(t)
        resumen.append((t, etiqueta))
    return resumen
    
# ---------CALCULAR MEDIA------------
media=calcular_media(temperaturas)
print("La temperatura media es de: ", media)

# ---------CALCULAR MAXIMA Y MINIMA----------------
maxima=calcular_maxima(temperaturas)
minima=calcular_minima(temperaturas)

print ("La temperatura máxima es: ", maxima)
print ("La temperatura mínima es: ", minima)

# --------HAY ALERTA--------------------

if hay_alerta(temperaturas, umbral_calor):
    print ("Aviso! Se ha superado el umbral de calor: ", umbral_calor)
else:
    print("Temperaturas por debajo del umbral de calor")


#-----------CONTADOR TEMPERATURA ALTAS-------------

contador=contar_temp_altas(temperaturas,umbral_calor)
print(f"Días por encima de {umbral_calor} grados: ", contador)


print("\n---------EVOLUCIÓN DÍA A DÍA-----------")

for i in range(1, len(temperaturas)):
    diferencia=temperaturas[i] - temperaturas[i-1]

    if diferencia>0:
        tendencia="🔺sube"
    elif diferencia<0:
        tendencia="🔻baja"
    else:
        tendencia="➖ igual"
    
    print(f"Día {i} -> Día {i+1}: {tendencia} ({round(diferencia, 2)} ºC)")


print("\n----------CLASIFICACIÓN DE LAS TEMPERATURAS---------------")

print(resumen_temperaturas(temperaturas))

