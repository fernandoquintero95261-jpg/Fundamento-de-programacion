import pandas as pd 

# cargar datos
ruta = "https://raw.githubusercontent.com/VMjavier/claseAnalisisDatos/refs/heads/main/veterinaria_colombia.csv"
df = pd.read_csv(ruta)

print("="*50)
print(df.head())
print("="*50)

print("="*50)
print(df.info())
print("="*50)

print("="*50)
print(df.describe())
print("="*50)

print("="*50)
print(df.columns())
print("="*50)

print("="*50)
print(id.isnull().sum())
print("="*50)

print(df.shape) #filas columnas)
print(df['Raza'])
print(df[['Raza' 'Especie']])
print(df[df['Raza'] == 'criollo'])