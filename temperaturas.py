temperaturas = [18.5, 21.2, 19.8, 23.1, 25.4]

print ("Las temperaturas registradas han sido las siguientes:", temperaturas)

#----------------------------------------------
media = sum(temperaturas) / len(temperaturas)

print("Temperatura media:", media)

# Pregunta 1 : ¿Cuál ha sido la temperatura máxima?
maxima_temperatura = max(temperaturas)

print("La temperatura máxima registrada ha sido de ", maxima_temperatura) 

# Pregunta 2 : ¿Cuál ha sido la temperatura mínima?
minima_temperatura = min(temperaturas)

print("La temperatura mínima registrada ha sido de ", minima_temperatura)

# Pregunta 3 : ¿Qué temperaturas son superiores a 22 ºC?
for temperatura in temperaturas:
    if temperatura > 22:
        print("Las temperaturas superiores a 22º han sido las siguientes:")
        print(temperatura)

# Pregunta 4: ¿Ha hecho algún día más de 25 ºC?
for temperatura in temperaturas:
    if temperatura > 25:
        print("Sí, ha habido una temperatura superior a 25 ºC")