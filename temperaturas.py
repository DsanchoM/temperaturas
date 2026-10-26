from analisis import (
    calcular_media,
    contar_mayores,
    clasificar_temperaturas,
    resumen_temperaturas
)

temperaturas=[18.5, 21.2, 19.8, 23.1, 25.4]

media=calcular_media(temperaturas)
maxima=max(temperaturas)
minima=min(temperaturas)


print(temperaturas)

print("La media de las temperaturas es de: ", media)
print("La maxima de las temperaturas es de: ", maxima)
print("La minima de las temperaturas es de: ", minima)

umbral_calor=22

if maxima>umbral_calor:
    print("Aviso! Se ha asuperado el umbral de calor: ", umbral_calor)
else:
    print("Todo en orden")



# contar temperaturas superiores al umbral
print(f"Dias por encima de los {umbral_calor} grados: ", contar_mayores(temperaturas,umbral_calor))

for i in range(1, len(temperaturas)):
    diferencia=temperaturas[i]-temperaturas[i-1]

    if diferencia>0:
        tendencia="🔺sube"
    elif diferencia<0:
        tendencia="baja"
    else:
        tendecia="igual"

    print(f"Dia {i} -> Dia {i+1}: {tendencia} {round(diferencia,2)} Grados")

print ("------CLASIFICACIÓN TEMPERATURAS------")

print(resumen_temperaturas(temperaturas))