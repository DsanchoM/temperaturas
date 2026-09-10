from temperaturas import calcular_media, obtener_maxima, obtener_minima

temperaturas_madrid = [18, 22, 25, 27, 24]
temperaturas_zaragoza = [15, 21, 28, 31, 26]

print ("Madrid")
print ("Media", calcular_media(temperaturas_madrid))
print ("Máxima", obtener_maxima(temperaturas_madrid))
print ("Mínima", obtener_minima(temperaturas_madrid))