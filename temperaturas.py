temperaturas=[18.5, 21.2, 19.8, 23.1, 25.4]

media=sum(temperaturas)/len(temperaturas)
maxima=max(temperaturas)
minima=min(temperaturas)


print(temperaturas)

print("La media de las temperaturas es de: ", media)
print("La maxima de las temperaturas es de: ", maxima)
print("La minima de las temperaturas es de: ", minima)

umbral_calor=30

if maxima>umbral_calor:
    print("Aviso! Se ha asuperado el umbral de calor: ", umbral_calor)
else:
    print("Todo en orden")