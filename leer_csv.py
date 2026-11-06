with open("datos.csv", "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    print(linea.strip())

print("\n----PARSEAR CADA LINEA--------\n")

registros = []
with open("datos.csv", "r", encoding="utf-8") as f:
    lineas = f.readlines()

# La primera línea son las cabeceras
cabeceras = lineas[0].strip().split(",")
print("Cabeceras:", cabeceras)

# El resto son datos
for linea in lineas[1:]:
       if not linea.strip():
             continue
       valores=linea.strip().split(",")
       registro=dict(zip(cabeceras,valores))
       registros.append(registro)

print(registros[0])    


print("\n ----------------HACEMOS LO MISMO CON PANDAS---------------\n")

import pandas as pd

df=pd.read_csv("datos.csv")

print(df.head())


print("\n----------------LEER CSV DESDE URL CON PANDAS------------------\n")

url="https://docs.google.com/spreadsheets/d/e/2PACX-1vQ6r03LVKMXCNtTQnl63_73xro7Q_IKSigjax0KaKPrQ28scYGPNZJMKmtHv5GcgP4pOWo9lNSNAnHK/pub?gid=0&single=true&output=csv"

df=pd.read_csv(url)

print(df)