
# Generación de funciones

# Calculo de la media
def calcular_media(temperaturas):
    return sum(temperaturas)/len(temperaturas)

# Obtención de la máxima
def obtener_maxima(temperaturas):
    return max(temperaturas)

# Obtención de la minima
def obtener_minima(temperaturas):
    return min(temperaturas)

temperaturas=[18.5, 21.2, 19.8, 23.1, 25.4]

media=calcular_media(temperaturas)
maxima=obtener_maxima(temperaturas)
minima=obtener_minima(temperaturas)

print("Media:",media)
print("Máxima:",maxima)
print("Mínima",minima)