
print("\n---------INFORME DE TEMPERATURAS-----------")

temperaturas=[18.5, 21.2, 19.8, 23.1, 25.4]
print("El registro de temperaturas es el siguiente: ", temperaturas)

media=sum(temperaturas)/len(temperaturas)

print("La temperatura media es de: ", media)

# Máximas y Mínimas
maxima=max(temperaturas)
minima=min(temperaturas)

print ("La temperatura máxima es: ", maxima)
print ("La temperatura mínima es: ", minima)

# Alarma de exceso de temperatura
umbral_calor=25

if maxima>umbral_calor:
    print("Aviso! Se ha superado el umbral de calor: ", umbral_calor)
else:
    print("Temperaturas por debajo del umbral de calor")

# Contabilizador
contador=0

for t in temperaturas:
    if t>20:
        contador=contador+1
print("Días por encima de 20 grados: ", contador)

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